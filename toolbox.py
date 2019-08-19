''' A toolbox with a number of useful methods. '''

import json
from matchupManager import MatchupManager
from pokemonType import PokemonType
from math import floor
from itertools import permutations, combinations, takewhile
from os import listdir

def parseMatchupsFile(path:str) -> list:
    ''' Reads the matchup json file.

    @param path: A string that represents the path to the matchups json file.
    
    @return: A list with every single Pokemon type
    
    @raise IOError: If something goes wrong in reading the file.

    '''

    output = []
    with open(path) as file:
        data = json.load(file)
    file.close()

    for (typeName, matchupData) in data.items():
        output.append(PokemonType(name=typeName, matchupData=matchupData))

    return output

def generateAllPossibleDualTypes(pokemonTypes:list, duplicates:bool=False) -> list:
    ''' Generates all the possible dual-types from the provided list of single type Pokemon.

    @param pokemonTypes: A list of single type PokemonTypes. Cannot be `None`.\n
    @param duplicates: If `True`, this method will includes duplicates (ie. Bug_Grass and Grass_Bug).

    @return: Returns a list containing all possible dual-type PokemonType instance combinations.
    
    '''
    if pokemonTypes is None:
        raise Exception("pokemonTypes cannot be None. You dummy.")

    output = []
    pairs = permutations(pokemonTypes, 2) if duplicates else combinations(pokemonTypes, 2)
    for (type1, type2) in takewhile(lambda pair: not pair[0].isDualType and not pair[1].isDualType, pairs): # Only take pairs that consist of only single types
        new_name = "{0}_{1}".format(type1.name, type2.name)
        output.append(PokemonType(name=new_name, type1=type1, type2=type2))
    return output

def getAllPokemonTypes(matchupsPath:str, duplicates:bool=False) -> list:
    ''' Gets all the Pokemon types. Both single and dual-type Pokemon.\n
    
    @param matchupsPath: The path to the matchup json file.

    @param duplicates: If this is True, then this function will include dual-types whose names are just switched around (ie. Water_Steel and Steel_Water).
    Single types are unaffected.

    @return: A list with all PokemonTypes (both single and dual-types).
    '''

    singleTypes = parseMatchupsFile(matchupsPath)
    dualTypes = generateAllPossibleDualTypes(singleTypes, duplicates)

    return singleTypes + dualTypes

def loadGenData(duplicates:bool=False) -> dict:
    base_path = "matchup_data/"
    file_names = listdir(base_path)
    def mapping_func(name:str) -> tuple:
        key = name.partition('-')[2].partition('.')[0]
        value = getAllPokemonTypes(base_path + name, duplicates)
        return (key, value)
    return dict(map(mapping_func, file_names))

def loadStatsData() -> dict:
    path = "stats_data/average_types.json"
    try:
        file = open(path, 'r')
        return json.load(file)
    finally:
        file.close()

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

if __name__ == "__main__":
    with open("./matchup_data/gen-7.json") as file:
        data = json.load(file)
    file.close()
    output = []
    for (name, matchupData) in data.items():
        output.append(PokemonType(name, matchupData))

    output[0].validate()
    raise Exception("")