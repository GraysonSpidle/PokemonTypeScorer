''' The main script that does the calculations. '''

from pokemonType import PokemonType
from math import e
from formulas import *

import json
import toolbox

# ====================
#  UTILITY FUNCTIONS
# ====================
def normalize(data:dict) -> None:
    ''' Normalizes the data.
    Puts all the data on a scale between 0 and 1.
    '''
    toAdd = float(list(data.items())[0][1])
    toAdd *= -1 if toAdd < 0 else 1
    for name in data.keys():
        data[name] += toAdd
    toDivide = float(list(data.values())[len(data) - 1])
    for name in data.keys():
        data[name] /= toDivide

def printRatings(ratings:dict) -> None:
    for (key, value) in ratings.items():
        print("{0}: {1}".format(key, value))
    print()

# ====================
#   RATING FUNCTIONS
# ====================
def _preliminaryRateTypes(pokemonTypes:dict, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> dict:
    ratings = {}
    for (name, pokemonType) in pokemonTypes.items():
        scores = pokemonType.rate(weights=(offensiveWeightFunc,defensiveWeightFunc))
        ratings[name] = sum(scores)

    ratings = dict(sorted(ratings.items(), key=lambda item: item[1])) # Sort from worst type to best type
    normalize(ratings)
    return ratings

def _rateAgain(pokemonType:PokemonType, ratings:dict, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> float:
    output = 0

    def _genericCalculator(matchupData:dict, weightFunc:callable) -> float:
        local_output = 0
        for (multiplier_str, typeNames) in matchupData.items():
            weight = weightFunc(float(multiplier_str))
            for typeName in typeNames:
                local_output += weight * ratings[typeName]

        return local_output
    
    output += _genericCalculator(pokemonType.offensiveMatchupData, offensiveWeightFunc)
    output += _genericCalculator(pokemonType.defensiveMatchupData, defensiveWeightFunc)

    return output

def _secondaryRateTypes(originalRatings:dict, pokemonTypes:dict, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> dict:
    output = {}
    for (name, pokemonType) in pokemonTypes.items():
        output[name] = _rateAgain(pokemonType, originalRatings, offensiveWeightFunc, defensiveWeightFunc)
    output = dict(sorted(output.items(), key=lambda item: item[1])) # Sort from worst type to best type
    normalize(output)
    return output

def rateTypes(pokemonTypes:dict, offensiveWeightFunc:callable, defensiveWeightFunc:callable) -> dict:
    vaccuum_ratings = _preliminaryRateTypes(pokemonTypes, offensiveWeightFunc, defensiveWeightFunc)
    # Now we're going to reward types that are resistant to types that have high ratings and penalize the types that are weak to types with high ratings.
    # Similarly, we'll also reward types that are strong against highly rated types and penalize types that are weak against highly rated types.
    contextual_ratings = _secondaryRateTypes(vaccuum_ratings, pokemonTypes, offensiveWeightFunc, defensiveWeightFunc)
    return contextual_ratings

# ====================
#         MAIN
# ====================
offensiveWeightFunc = offensivePiecewiseWeightFunc
defensiveWeightFunc = defensivePiecewiseWeightFunc

gen_data = toolbox.loadGenData(True)
ratings_across_gens = {}
for (gen_num, data) in gen_data.items():
    gen_ratings = rateTypes(data, offensiveWeightFunc, defensiveWeightFunc)
    for name in data.keys():
        if name not in ratings_across_gens.keys():
            ratings_across_gens[name] = {}
        
        ratings_across_gens[name][gen_num] = gen_ratings[name]

for gen_num in gen_data.keys():
    for (name, data) in ratings_across_gens.items():
        if gen_num not in data.keys():
            data[gen_num] = "Not Introduced"

file = open("results.json", 'w')
file.write(json.dumps(ratings_across_gens, sort_keys=True, indent=3))
file.close()

