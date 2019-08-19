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

def rateTypes(pokemonTypes:list, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> dict:
    ''' Rating the pokemon types in a vaccuum.  '''
    vaccuum_ratings = _preliminaryRateTypes(pokemonTypes, offensiveWeightFunc, defensiveWeightFunc)
    ''' Now we're going to reward types that are resistant to types that have high ratings and penalize the types that are weak to types with high ratings.
    Similarly, we'll also reward types that are strong against highly rated types and penalize types that are weak against highly rated types. '''
    contextual_ratings = _secondaryRateTypes(vaccuum_ratings, pokemonTypes, offensiveWeightFunc, defensiveWeightFunc)
    return contextual_ratings

# ====================
#         MAIN
# ====================
settings.generation_number = 7

offensiveWeightFunc = offensivePiecewiseWeightFunc
defensiveWeightFunc = defensivePiecewiseWeightFunc

# Load data
pokemonTypes = toolbox.getAllPokemonTypes("./matchup_data/gen-{}.json".format(settings.generation_number))
stageMultiplierData = settings.loadStageMultiplierData()
statsData = settings.loadStatsData()

# Rate the types
type_ratings = rateTypes(pokemonTypes, offensiveWeightFunc, defensiveWeightFunc)

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
    file.write(html.format(settings.generation_number, html_table_data))
file.close()
