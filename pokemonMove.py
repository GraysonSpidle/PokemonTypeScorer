from pokemonType import PokemonType

class PokemonMove:
    CATEGORY_PHYSICAL = 0
    CATEGORY_SPECIAL = 1
    CATEGORY_STATUS = 2

    def __init__(self, name:str, Type:PokemonType, category:int, power:int, accuracy:int, isSingleTarget:bool):
        self.name = name
        self.Type = Type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.isSingleTarget = isSingleTarget
