from settings import generation_number

class PokemonStat:
    def __init__(self, name:str, value:int, isSpecial:bool, isBattleExclusive:bool, baseStages:int=0):
        ''' Constructor for a Pokemon stat.

        Parameters
        ----------

        name : str
            The name of the stat.

        value : int
            The value of the stat.

        isSpecial : bool
            Indicates if this stat is a special stat (special attack or special defense)
        
        isBattleExclusive : bool
            Indicates if this stat only comes into play during a battle (evasion or accuracy)
        
        '''

        self.name = name
        self.value = value
        self.isSpecial = isSpecial
        self.isBattleExclusive = isBattleExclusive
        self.stages = baseStages
        self._baseStages = baseStages

    def _getStageMultiplier(self) -> float:
        if any(_name == self.name.lower() for _name in ["attack", "defense", "special attack", "special defense", "speed"]):
            if generation_number < 3:
                


    def __getattribute__(self, name):
        # Note that prior to Generation III, no stat can fall below 1 or rise above 999; any further modifiers will fail regardless of whether the stat is at -6 or +6 or not.
        if name == "value":
            pass

    def raiseStage(self, n:int):
        if n <= 0:
            raise Exception("Cannot raise stat by a non-positive and non-zero number of stages")
        self.stages = min(self.stages + n, 6)
    
    def lowerStage(self, n:int):
        if n >= 0:
            raise Exception("Cannot lower stat by a non-negative and non-zero number of stages")
        self.stages = max(self.stages - n, -6)

    def resetStages(self):
        self.stages = self._baseStages

