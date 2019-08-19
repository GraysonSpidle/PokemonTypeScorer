from pokemonMove import PokemonMove

class MovesManager:
    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def moves(self) -> list:
        raise NotImplementedError


    