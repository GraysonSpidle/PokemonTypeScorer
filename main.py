from sys import argv
from pokemonType import PokemonType
import toolbox

if len(argv) > 1:
    matchupsPath = str(argv[1])
else:
    matchupsPath = "gen-vii-type-matchups.json"

def offensiveWeightFunc(multiplier_str:str) -> float:
    multiplier = float(multiplier_str)
    equation1 = lambda mult: (mult - 1.5)**(2) + 1
    equation2 = lambda mult: -(-mult + 1.5)**(3/2) - 1
    return equation2(multiplier) if multiplier < 1.5 else equation1(multiplier)

def defensiveWeightFunc(multiplier_str:str) -> float:
    multiplier = float(multiplier_str)
    equation1 = lambda mult: -(mult - 1)**(3/2) - 1
    equation2 = lambda mult: (-mult + 1)**(2/3) + 1
    return equation2(multiplier) if multiplier < 1 else equation1(multiplier)

pokemonTypes = toolbox.getAllPokemonTypes(matchupsPath)

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

def rateTypes() -> dict:
    ratings = {}
    for (name, pokemonType) in pokemonTypes.items():
        ratings[name] = pokemonType.rate(weights=(offensiveWeightFunc,defensiveWeightFunc))

    ratings = dict(sorted(ratings.items(), key=lambda item: item[1])) # Sort from worst type to best type
    normalize(ratings)
    return ratings

ratings = rateTypes() # These are the ratings in a vaccuum.
# printRatings(ratings)

# Now we're going to reward types that are resistant to types that have high ratings and penalize the types that are weak to types with high ratings.
# Similarly, we'll also reward types that are strong against highly rated types and penalize types that are weak against highly rated types.

def rateAgain(pokemonType:PokemonType, ratings:dict) -> float:
    output = 0
    for (multiplier, typeNames) in pokemonType.defensiveMatchupData.items():
        weight = defensiveWeightFunc(multiplier)
        for typeName in typeNames:
            output += weight * ratings[typeName]
    return output

def rateTypesAgain(originalRatings:dict) -> dict:
    output = {}
    for (name, pokemonType) in pokemonTypes.items():
        output[name] = rateAgain(pokemonType, originalRatings)
    output = dict(sorted(output.items(), key=lambda item: item[1])) # Sort from worst type to best type
    normalize(output)
    return output

newRatings = rateTypesAgain(ratings)
printRatings(newRatings)
