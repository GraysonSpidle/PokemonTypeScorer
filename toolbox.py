''' A toolbox with a number of useful methods. '''

import json
from matchupManager import MatchupManager
from pokemonType import PokemonType
from math import floor

def parseMatchupsFile(path:str) -> dict:
    ''' Reads the matchup json file and spits out a dictionary with PokemonTypes (single types only) mapped to string representations of their names.

    Parameters
    ----------

    path : str
        The path to the matchups json file.

    '''
    output = {}
    file = open(path)
    data = json.load(file)
    file.close()

    for (typeName, matchupData) in data.items():
        output[typeName] = PokemonType(name=typeName, matchupData=matchupData)

    return output

def generateAllPossibleDualTypes(pokemonTypes:list) -> list:
    ''' Generates all the possible dual-types from the provided list of single type Pokemon.
    This includes duplicates (ie. Bug_Grass and Grass_Bug).
    
    Parameters
    ----------

    pokemonTypes : list
        A list of single typed PokemonTypes
    
    '''
    output = list()
    for firstType in pokemonTypes:
        if not firstType.isDualType:
            for secondType in pokemonTypes:
                if firstType is secondType or secondType.isDualType:
                    continue
                new_name = "{0}_{1}".format(firstType.name, secondType.name)
                output.append(PokemonType(name=new_name, type1=firstType, type2=secondType))
    return output

def getAllPokemonTypes(matchupsPath:str, duplicates:bool=False) -> dict:
    ''' Gets all the Pokemon types. Both single and dual-type Pokemon.\n

    Parameters
    ----------

    matchupsPath : str
        The path to the matchup json file.

    duplicates : bool, optional
        If this is True, then this function will include dual-types whose names are just switched around (ie. Water_Steel and Steel_Water).
        Single types are unaffected.

    
    Returns a dictionary with the PokemonType's name (string) as the key and the PokemonType object as the value.
    '''

    singleTypes = parseMatchupsFile(matchupsPath)
    dualTypes = generateAllPossibleDualTypes(singleTypes.values())
    output = singleTypes

    def _switchTypeName(typeName:str) -> str:
        split = typeName.split("_")
        return "{0}_{1}".format(split[1], split[0])

    for pokemonType in dualTypes:
        if pokemonType.isDualType and not duplicates: # Checking for duplicates
            if not _switchTypeName(pokemonType.name) in output.keys():
                output[pokemonType.name] = pokemonType
        else:
            output[pokemonType.name] = pokemonType
    return output

