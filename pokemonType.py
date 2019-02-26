''' Houses the PokemonType class '''

from matchupManager import MatchupManager

class PokemonType(MatchupManager):
    ''' This is the class used to represent different types of Pokemon found in the popular Pokemon games by GameFreak.
    It encapsulates a dictionary that holds type matchup data relevant to the particular type the PokemonType instance is
    representing.\n

    Note: The type matchup data assumes that Pokemon types can only perform moves belonging to their respective type. I know this is incorrect,
    because you can go the beginning of the very first Pokemon game and prove me wrong. As a result, any data that originated
    from any offensive type matchup datasets inherits this assumption and the results should not be taken seriously.

    '''

    @staticmethod
    def combineMatchupData(type1:MatchupManager, type2:MatchupManager) -> tuple:
        ''' Combines the matchup data of two single type MatchupManager objects resulting in a dual-type.\n

        @param type1: The first type to use when creating the new dual-type. This cannot be a dual-type.
        @param type2: The second type to use when creating the new dual-type. This cannot be a dual-type.

        @return: A tuple containing the offensive and defensive matchup data.

        @raise ValidationError: If either of the two types are invalid.

        '''

        # ====================================
        #         PARAMETER VALIDATION        
        # ====================================
        if type1.isDualType or type2.isDualType:
            raise Exception("Cannot make a dual-type with a dual-type.")
        type1.validate()
        type2.validate()
        
        # ====================================
        #         INITIALIZING VALUES        
        # ====================================
        newOffensiveMatchupData = {}
        newDefensiveMatchupData = {}
        allTypeNames = []
        for typeNames in type1.offensiveMatchupData.values():
            allTypeNames += typeNames

        # ====================================
        #       WHERE THE MAGIC HAPPENS
        # ====================================
        for typeName in allTypeNames:
            type1Multipliers = type1.getMultipliers(typeName)
            type2Multipliers = type2.getMultipliers(typeName)

            offensiveMultiplier = str(max(float(type1Multipliers[0]), float(type2Multipliers[0])))
            defensiveMultiplier = str(float(type1Multipliers[1]) * float(type2Multipliers[1]))

            if not offensiveMultiplier in newOffensiveMatchupData.keys():
                newOffensiveMatchupData[offensiveMultiplier] = []
            if not defensiveMultiplier in newDefensiveMatchupData.keys():
                newDefensiveMatchupData[defensiveMultiplier] = []
            
            newOffensiveMatchupData[offensiveMultiplier].append(typeName)
            newDefensiveMatchupData[defensiveMultiplier].append(typeName)

        return (newOffensiveMatchupData, newDefensiveMatchupData)

    def __init__(self, name:str, matchupData:dict=None, type1:MatchupManager=None, type2:MatchupManager=None, **kwargs):
        ''' The method for constructing a new PokemonType instance which takes in 1 required parameters and 3 optional parameters.

        This class has 2 constructors:\n
        1. PokemonType(name,matchupData): This is the single type constructor
        2. PokemonType(name,type1,type2): This is the dual-type constructor\n
        Failure to choose one of these will result in a thrown exception. If both are selected, then this method will choose
        the first constructor

        @param name: This is a string that is the name of the Pokemon type.

        @param matchupData: A dict of Matchup instances that describe this PokemonType's matchups. For ease of access this method indexes
        all the Matchup instances by their MatchupType. If you use this parameter, then the PokemonType will be single type.
        
        @param type1: A MatchupManager that represents the dual-type's first type.
        @param type2: A MatchupManager that represents the dual-type's second type.
        '''
        self._name = name
        self._isDualType = False
        if not matchupData is None:
            self._matchupData = matchupData
            self._type1 = self
            self._type2 = None
        elif not type1 is None and not type2 is None:
            offensive, defensive = PokemonType.combineMatchupData(type1, type2)
            self._matchupData = {"offensive": offensive, "defensive": defensive}
            self._type1 = type1
            self._type2 = type2
            self._isDualType = True
        else:
            raise Exception("Pick one of the 2 constructors")
        
    @property
    def name(self) -> str:
        ''' The name of this type. '''
        return self._name

    @property
    def isDualType(self) -> bool:
        ''' A boolean representing this type's dual-type status. True if it is a dual-type. '''
        return self._isDualType

    @property
    def matchupData(self) -> dict:
        ''' Returns this PokemonType's matchup data. '''
        return self._matchupData

    @property
    def firstType(self) -> MatchupManager:
        ''' A MatchupManager that represents this PokemonType's first type. '''
        return self._type1

    @property
    def secondType(self) -> MatchupManager:
        ''' A MatchupManager that represents this PokemonType's second type.
        This will be None if isDualType is False.
        '''
        return self._type2

    

