''' A toolbox with a number of useful methods. '''

import json
from matchupManager import MatchupManager
from pokemonType import PokemonType
from math import floor
from itertools import permutations, combinations, takewhile

def parseMatchupsFile(path:str) -> dict:
    ''' Reads the matchup json file.

    @param path: A string that represents the path to the matchups json file.
    
    @return: A dictionary with PokemonTypes (single types only) mapped to string representations of their names.
    
    @raise IOError: If something goes wrong in reading the file.

    '''

    output = {}
    with open(path) as file:
        data = json.load(file)
    file.close()

    for (typeName, matchupData) in data.items():
        output[typeName] = PokemonType(name=typeName, matchupData=matchupData)

    return output

def generateAllPossibleDualTypes(pokemonTypes:list, duplicates:bool=False) -> list:
    ''' Generates all the possible dual-types from the provided list of single type Pokemon.

    @param pokemonTypes: A list of single type PokemonTypes
    @param duplicates: If True, this method will includes duplicates (ie. Bug_Grass and Grass_Bug).

    @return: Returns a list containing all possible dual-type PokemonType instance combinations.
    
    '''
    output = list()
    pairs = permutations(pokemonTypes, 2) if duplicates else combinations(pokemonTypes, 2)
    for (type1, type2) in takewhile(lambda pair: not pair[0].isDualType and not pair[1].isDualType, pairs): # Only take single types
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
    dualTypes = generateAllPossibleDualTypes(singleTypes.values(), duplicates)

    return singleTypes + dualTypes

