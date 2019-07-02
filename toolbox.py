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

def getAllPokemonTypes(matchupsPath:str, duplicates:bool=False) -> dict:
    ''' Gets all the Pokemon types. Both single and dual-type Pokemon.\n
    
    @param matchupsPath: The path to the matchup json file.

    @param duplicates: If this is True, then this function will include dual-types whose names are just switched around (ie. Water_Steel and Steel_Water).
    Single types are unaffected.

    @return: A dictionary with the PokemonType's name (string) as the key and the PokemonType object as the value.
    '''

    singleTypes = parseMatchupsFile(matchupsPath)
    dualTypes = generateAllPossibleDualTypes(singleTypes, duplicates)

    return dict((pokemonType.name, pokemonType) for pokemonType in (singleTypes + dualTypes))

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
