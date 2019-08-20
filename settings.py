import os
import json
from pokemonType import PokemonType

def _merge_dictionaries(left:dict, right:dict) -> None:
    ''' In place merging. The right dictionary overrides the left dictionary. '''
    for key in right.keys():
        left[key] = right[key]

def _loadSettingData(path:str, generation_number:int) -> dict:
    mapped = dict((file_name.split('-')[1].split('.')[0], file_name) for file_name in os.listdir(path))
    output = {}
    ''' Keep overriding stuff with _merge_dictionaries until you reach a file whose gen number exceeds or equals the generation_number variable '''
    for (gen_num, file_name) in mapped.items():
        if int(gen_num) <= generation_number:
            file = open(path + file_name, 'r')
            _merge_dictionaries(output, json.load(file))
            file.close()
        else:
            break
    return output

def loadStageMultiplierData(path:str="/stage_multipliers/", generation_number:int=7) -> dict:
    return _loadSettingData(os.curdir + path, generation_number)

def loadMatchupData(path:str="/matchup_data/", generation_number:int=7) -> dict:
    rawData = _loadSettingData(os.curdir + path, generation_number)
    # Encapsulating the data into PokemonTypes
    output = {}
    for (name, type_data) in rawData.items():
        output[name] = PokemonType(name, type_data)
    del rawData
    return output

def loadStatsData(path:str="/stats_data/average_types.json") -> dict:
    try:
        file = open(os.curdir + path, 'r')
        return json.load(file)
    finally:
        file.close()