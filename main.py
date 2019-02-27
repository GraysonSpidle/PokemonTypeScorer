from sys import argv
from pokemonType import PokemonType
import toolbox
from math import e

# ====================
#     COMMAND LINE
# ====================

if len(argv) > 1:
    matchupsPath = str(argv[1])
else:
    matchupsPath = "gen-vii-type-matchups.json"

# ====================
#   WEIGHT FUNCTIONS
# ====================
def offensiveWeightFunc(multiplier:float) -> float:
    equation1 = lambda mult: (mult - 1.5)**(2) + 1
    equation2 = lambda mult: -(2.2*(1.5-mult)**0.5)-(0.5*mult)-0.25
    return equation2(multiplier) if multiplier < 1.5 else equation1(multiplier)

def defensiveWeightFunc(multiplier:float) -> float:
    equation1 = lambda mult: -(mult - 1)**(3/2) - 1
    equation2 = lambda mult: (-mult + 1)**(2/3) + 1
    return equation2(multiplier) if multiplier < 1 else equation1(multiplier)

# ====================
#  UTILITY FUNCTIONS
# ====================
def normalize(data:dict):
    ''' Normalizes the data '''
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
def rateTypes(pokemonTypes:dict) -> dict:
    ratings = {}
    for (name, pokemonType) in pokemonTypes.items():
        scores = pokemonType.rate(weights=(offensiveWeightFunc,defensiveWeightFunc))
        print(name, scores)
        ratings[name] = sum(scores)

    ratings = dict(sorted(ratings.items(), key=lambda item: item[1])) # Sort from worst type to best type
    normalize(ratings)
    return ratings

def rateAgain(pokemonType:PokemonType, ratings:dict) -> float:
    output = 0

    def genericCalculator(matchupData:dict, weightFunc:callable) -> float:
        local_output = 0
        for (multiplier_str, typeNames) in matchupData.items():
            weight = weightFunc(float(multiplier_str))
            for typeName in typeNames:
                local_output += weight * ratings[typeName]

        return local_output
    
    output += genericCalculator(pokemonType.offensiveMatchupData, offensiveWeightFunc)
    output += genericCalculator(pokemonType.defensiveMatchupData, defensiveWeightFunc)

    return output

def rateTypesAgain(originalRatings:dict, pokemonTypes:dict) -> dict:
    output = {}
    for (name, pokemonType) in pokemonTypes.items():
        output[name] = rateAgain(pokemonType, originalRatings)
    output = dict(sorted(output.items(), key=lambda item: item[1])) # Sort from worst type to best type
    normalize(output)
    return output

# ====================
#         MAIN
# ====================
pokemonTypes = toolbox.getAllPokemonTypes(matchupsPath) # Get all pokemon types

ratings = rateTypes(pokemonTypes) # These are the ratings in a vaccuum.
printRatings(ratings)

# Now we're going to reward types that are resistant to types that have high ratings and penalize the types that are weak to types with high ratings.
# Similarly, we'll also reward types that are strong against highly rated types and penalize types that are weak against highly rated types.

# newRatings = rateTypesAgain(ratings, pokemonTypes)
# printRatings(newRatings)
