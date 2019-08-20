''' The main script that does the calculations and spits it out into an html file for easy viewing. '''

from matchupManager import MatchupManager
from pokemonType import PokemonType
from pokemon import Pokemon
from pokemonMove import PokemonMove
from math import e
from formulas import *

import json
import toolbox
import settings
import os

# ====================
#   RATING FUNCTIONS
# ====================
def _preliminaryRateTypes(pokemonTypes:list, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> dict:
    ratings = {}
    ''' Iterating through all the pokemon types and getting their ratings in a vaccuum. '''
    for pokemonType in pokemonTypes:
        offensiveScore, defensiveScore = pokemonType.rate(weights=(offensiveWeightFunc,defensiveWeightFunc))
        ratings[pokemonType.name] = offensiveScore + defensiveScore

    ratings = dict(sorted(ratings.items(), key=lambda item: item[1])) # Sort from worst type to best type
    toolbox.normalize(ratings) # Normalize the output
    return ratings

def _rateInContext(obj:MatchupManager, ratings:dict, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> float:
    output = 0

    def _genericCalculator(matchupData:dict, weightFunc:callable) -> float:
        local_output = 0
        for (multiplier_str, typeNames) in matchupData.items():
            weight = weightFunc(float(multiplier_str))
            for typeName in typeNames:
                local_output += weight * ratings[typeName]

        return local_output
    
    output += _genericCalculator(obj.offensiveMatchupData, offensiveWeightFunc)
    output += _genericCalculator(obj.defensiveMatchupData, defensiveWeightFunc)

    return output

def _secondaryRateTypes(originalRatings:dict, pokemonTypes:list, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> dict:
    ''' Rates the pokemon types again except it rewards types that are resistant to types that have high ratings and penalizes the types
    that are weak to types with high ratings. Additionally, we'll reward types that are strong against highly rated types and penalize 
    types that are weak against highly rated types. 
    
    Parameters
    ----------
    originalRatings : dict
        The ratings of the types in a vaccuum.

    pokemonTypes : list
        The pokemon types to rate
    
    offensiveWeightFunc : callable
        The weight function that will be applied to weight the offensive score. It takes in a float (the multiplier) and returns another float.
    
    defensiveWeightFunc : callable
        The weight function that will be applied to weight the defensive score. It takes in a float (the multiplier) and returns another float.
    
    '''
    output = {}
    for pokemonType in pokemonTypes:
        output[pokemonType.name] = _rateInContext(pokemonType, originalRatings, offensiveWeightFunc, defensiveWeightFunc)
    output = dict(sorted(output.items(), key=lambda item: item[1])) # Sort from worst type to best type
    toolbox.normalize(output)
    return output

def _rateTypes(pokemonTypes:list, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> dict:
    ''' Rating the pokemon types in a vaccuum.  '''
    vaccuum_ratings = _preliminaryRateTypes(pokemonTypes, offensiveWeightFunc, defensiveWeightFunc)
    ''' Now we're going to reward types that are resistant to types that have high ratings and penalize the types that are weak to types with high ratings.
    Similarly, we'll also reward types that are strong against highly rated types and penalize types that are weak against highly rated types. '''
    contextual_ratings = _secondaryRateTypes(vaccuum_ratings, pokemonTypes, offensiveWeightFunc, defensiveWeightFunc)
    return contextual_ratings


def rateTypesInGen(generation_number:int, offensiveWeightFunc:callable, defensiveWeightFunc:callable, matchupDataDir:str="./matchup_data/", writeToFile:bool=True):
    # Loading the data
    pokemonTypes = toolbox.getAllPokemonTypes("{}/gen-{}.json".format(matchupDataDir, generation_number))

    # Rating the types
    type_ratings = _rateTypes(pokemonTypes, offensiveWeightFunc, defensiveWeightFunc)

    if not writeToFile:
        return type_ratings
    
    # Putting the ratings into html so it's easier to read
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gen {0} Results</title>
    </head>
    <body>
        <h1>Gen {0} Results</h1>
        <table>
            <tr>
                <th>Pokemon Type Name</th>
                <th>Rating</th>
            </tr>
            {1}
        </table>
    </body>
    </html>
    """

    html_table_data = ""
    for (name, score) in type_ratings.items():
        html_table_data += "<tr><td>{}</td><td>{}</td></tr>\n".format(name, score)

    with open("type_results.html", 'w') as file:
        file.write(html.format(generation_number, html_table_data))
    file.close()
    return type_ratings

def rateTypesAcrossAllGens(offensiveWeightFunc:callable, defensiveWeightFunc:callable, matchupDataDir:str="./matchup_data/", writeToFile:bool=True):
    mapped = dict((file_name.split('-')[1].split('.')[0], file_name) for file_name in os.listdir(matchupDataDir))
    output = {}
    for (gen_number_str, file_name) in mapped.items():
        output[gen_number_str] = rateTypesInGen(int(gen_number_str), offensiveWeightFunc, defensiveWeightFunc, matchupDataDir=matchupDataDir, writeToFile=False)
    
    if not writeToFile:
        return output

    # Putting the ratings into html so it's easier to read
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Results Across All Generations</title>
    </head>
    <body>
        <h1>Results Across All Generations</h1>
        <h3>Hint: click on the headers to sort</h3>
        <table id="resultsTable">
            <tr>
                <th onclick="sortTable(0)" style="cursor: pointer;">Pokemon Type Name</th>
                {0}
            </tr>
            {1}
        </table>
        <script>{2}</script>
    </body>
    </html>
    """

    html_table_headers = ""
    for gen_number_str in output.keys():
        html_table_headers += "<th onclick=\"sortTable({0})\" style=\"cursor: pointer;\">Gen {0}</th>".format(gen_number_str)

    alphabetized_list_of_pokemon_types = []
    for data_set in output.values():
        alphabetized_list_of_pokemon_types = sorted(toolbox.union(alphabetized_list_of_pokemon_types, data_set.keys()))

    html_table_data = ""
    for pokemon_type_name in alphabetized_list_of_pokemon_types:
        html_table_data += "<tr><td>{}</td>".format(pokemon_type_name)
        for gen_number_str in mapped.keys():
            try:
                result = output[gen_number_str][pokemon_type_name]
            except KeyError:
                result = "Not Introduced"
            html_table_data += "<td>{}</td>".format(result)
        html_table_data += "</tr>"
    
    html_scripts = ""
    with open("scripts.js") as file:
        html_scripts = file.read()
    file.close()

    with open("type_results.html", 'w') as file:
        file.write(html.format(html_table_headers, html_table_data, html_scripts))
    file.close()
    return output

# ====================
#         MAIN
# ====================
offensiveWeightFunc = offensivePiecewiseWeightFunc
defensiveWeightFunc = defensivePiecewiseWeightFunc

rateTypesAcrossAllGens(offensiveWeightFunc, defensiveWeightFunc)

