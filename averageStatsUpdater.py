from requests import get
from json import dump

def getPokemonUrls() -> list:
    response = get("https://www.pokeapi.co/api/v2/pokemon/", params={"limit": 2**32}).json()
    print("Number of Urls:", response["count"])
    return [result["url"] for result in response["results"]]

def readStat(stat_json:dict) -> tuple:
    return (stat_json["stat"]["name"].replace("-", "_"), stat_json["base_stat"])

def readStats(stats:list) -> list:
    return [readStat(stat) for stat in stats]

def readType(type_json:dict) -> tuple:
    return (type_json["slot"], type_json["type"]["name"].capitalize())

def readTypes(types:list) -> list:
    return [readType(type_json) for type_json in types]

def getPokemonStatsAndTypes(pokemon_url:str) -> tuple:
    pokemon = get(pokemon_url).json()
    stats = readStats(pokemon["stats"])
    types = readTypes(pokemon["types"])
    if len(types) == 1: # If it's a single type
        slot, name = types[0]
    elif len(types) == 2: # If it's a dual-type
        type1, type2 = types # These aren't necessarily the first and second types
        name = "{}_{}".format(type1[1] if type1[0] == 1 else type2[1], type1[1] if type1[0] == 2 else type2[1])
    else: # Something went wrong
        raise Exception("Something went wrong when getting Pokemon stats and types.")
    
    print("Simplified", pokemon_url)
    return (name, dict(stats))

def mergeEntries(left:dict, right:dict) -> dict:
    return dict((key, left[key] + right[key]) for key in left.keys())

if __name__ == "__main__":
    file_path = "stats_data/average_types.json"

    print("Getting Pokemon Urls...")
    pokemon_urls = getPokemonUrls()

    print("Simplifying Pokemon data into stats and types...")
    simplified_pokemon_data = [getPokemonStatsAndTypes(pokemon_url) for pokemon_url in pokemon_urls]
    del pokemon_urls

    print("Averaging the data...")
    average_data = {}
    for (name, data) in simplified_pokemon_data:
        if name in average_data.keys():
            n = average_data[name]['n'] + 1
            average_data[name] = mergeEntries(data, average_data[name])
        else:
            n = 1
            average_data[name] = data
        average_data[name]['n'] = n

    # Dividing each stat in each type by its n value
    for name in average_data.keys():
        n = average_data[name]['n']
        average_data[name] = dict((key, value / n) for (key, value) in average_data[name].items())
        del average_data[name]['n']


    print("Writing the data...")
    file = open(file_path, 'w')
    dump(average_data, file, indent=3, sort_keys=True)
    file.close()
    print("Done.")
