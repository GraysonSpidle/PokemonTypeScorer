from matchupManager import MatchupManager
from pokemonType import PokemonType
from pokemonMove import PokemonMove
from statsManager import StatsManager
from movesManager import MovesManager

class Pokemon(MatchupManager, StatsManager, MovesManager):

    @staticmethod
    def combineOffensiveMatchupData(*moves) -> dict:
        if len(moves) == 0:
            return None
        types = [move.Type for move in moves]
        output = types[0]
        for i in range(1,len(types)):
            offensive, defensive = PokemonType.combineMatchupData(output, types[i])
            # This is a bit of a white lie, b/c this constructor is supposed to be used for single-types, but we're only using it for the offensive data
            output = PokemonType("If you're reading this, then something messed up", {"offensive": offensive, "defensive": defensive})
        return output.offensiveMatchupData

    def __init__(self, name:str, pokemon_type:PokemonType, moves:list=None, **kwargs):
        StatsManager.__init__(self, **kwargs)
        self._name = name
        self.pokemon_type = pokemon_type
        self._moves = []
        if moves is None:
            # Defaulting to generic moves that match the type with average power
            if pokemon_type.isDualType:
                self._moves = [
                    PokemonMove("Generic Physical {} Move".format(pokemon_type.firstType.name), pokemon_type.firstType, PokemonMove.CATEGORY_PHYSICAL, 60, 100, True),
                    PokemonMove("Generic Special {} Move".format(pokemon_type.firstType.name), pokemon_type.firstType, PokemonMove.CATEGORY_SPECIAL, 60, 100, True),
                    PokemonMove("Generic Physical {} Move".format(pokemon_type.secondType.name), pokemon_type.secondType, PokemonMove.CATEGORY_PHYSICAL, 60, 100, True),
                    PokemonMove("Generic Special {} Move".format(pokemon_type.secondType.name), pokemon_type.secondType, PokemonMove.CATEGORY_SPECIAL, 60, 100, True)
                ]
            else:
                self._moves = [
                    PokemonMove("Generic Physical {} Move".format(pokemon_type.name), pokemon_type, PokemonMove.CATEGORY_PHYSICAL, 60, 100, True),
                    PokemonMove("Generic Special {} Move".format(pokemon_type.name), pokemon_type, PokemonMove.CATEGORY_SPECIAL, 60, 100, True),
                    PokemonMove("Generic Physical {} Move".format(pokemon_type.name), pokemon_type, PokemonMove.CATEGORY_PHYSICAL, 60, 100, True),
                    PokemonMove("Generic Special {} Move".format(pokemon_type.name), pokemon_type, PokemonMove.CATEGORY_SPECIAL, 60, 100, True)
                ]
        else:
            self._moves = moves

    @property
    def name(self) -> str:
        return self._name

    @property
    def isDualType(self) -> bool:
        ''' A boolean representing this type's dual-type status. True if it is a dual-type. '''
        return self.pokemon_type.isDualType

    @property
    def offensiveMatchupData(self) -> dict:
        if not '_newOffensiveMatchupData' in dir(self):
            self._newOffensiveMatchupData = Pokemon.combineOffensiveMatchupData(*self.moves)
        return self._newOffensiveMatchupData

    @property
    def matchupData(self) -> dict:
        ''' Returns this PokemonType's matchup data. '''
        return self.pokemon_type.matchupData

    @property
    def firstType(self) -> MatchupManager:
        ''' A MatchupManager that represents this PokemonType's first type.\n
        If `isDualType` is `False`, this property will be this PokemonType instance.\n
        If `isDualType` is `True`, this property will be the first type given when this object was constructed.
        '''
        return self.pokemon_type.firstType

    @property
    def secondType(self) -> MatchupManager:
        ''' A MatchupManager that represents this PokemonType's second type.\n
        If `isDualType` is `False`, this property will be `None`.\n
        If `isDualType` is `True`, this property will be the second type given when this object was constructed.
        '''
        return self.pokemon_type.secondType

    @property
    def moves(self) -> list:
        return self._moves

    def validate(self):
        MatchupManager.validate(self)
        StatsManager.validate(self)

