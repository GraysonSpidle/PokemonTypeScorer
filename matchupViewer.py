''' A utility script that allows you to view Pokemon type matchup data easier.

@param arg0: This is the path to a specific generation type matchup file.

'''

from sys import argv
from threading import Thread
from pokemonType import PokemonType
import toolbox

# ====================
#     COMMAND LINE
# ====================
if len(argv) > 1:
    matchupsPath = str(argv[1])
else:
    matchupsPath = "matchup_data/gen-7.json"


# ====================
#    INITIALIZATION
# ====================
# Loading all the Pokemon types
try:
    allPokemonTypes = toolbox.getAllPokemonTypes(matchupsPath, duplicates=True)
except OSError:
    print("{0} is an invalid path.".format(matchupsPath))
    exit(-1)
except IOError:
    print("There was an issue when reading the file.")
    exit(-1)

def displayer(toDisplay:PokemonType):
    ''' The displayer function each thread will use when called. '''
    toDisplay.display()

# ====================
#         MAIN
# ====================
if __name__ == "__main__":
    print("Enter an empty line to exit")
    while True:
        try:
            name = input("Name of type: ").capitalize()

            # Manipulating the input to fit the formatting of the data
            if name == "":
                break
            elif ' ' in name or '_' in name: # it's a dual-type
                if ' ' in name:
                    split_char = ' '
                elif '_' in name:
                    split_char = '_'
                splitted = name.split(split_char)
                name = "{0}_{1}".format(splitted[0], splitted[1].capitalize())
            
            # Starting the thread
            thread = Thread(target=displayer, args=[allPokemonTypes[name]], daemon=True)
            thread.start()
        except KeyError:
            print("Error: \"{0}\" is not a valid Pokemon type.\n".format(name))

