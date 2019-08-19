''' Houses the MatchupManager class. '''
from itertools import chain
from tkinter import Tk, Label, Y, N, LEFT, RIGHT, TOP, Grid, N, NW
from errors import ValidationError
import json

class MatchupManager:
    ''' This is the class that manages Matchups (wow). Its primary purpose is to provide the framework 
    needed to rate types and Pokemon based on their type matchups. In essence, this
    class encapsulates a number of dictionaries and provides a standard way of accessing them. It also
    adds some convenience methods.

    The dictionary that each instance encapsulates is structured as follows:
        key : str
            The key is either "offensive" or "defensive".
        value : dict
            A dictionary of multipliers (strings) mapped to lists of PokemonType names (strings).
    
    '''

    @staticmethod
    def colors() -> dict:
        return json.load(open("colors.json"))

    @staticmethod
    def defaultWeights() -> tuple:
        ''' Returns a tuple containing two lambda functions that return a float. '''
        return (lambda mult: float(mult), lambda mult: float(mult))

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def matchupData(self) -> dict:
        raise NotImplementedError

    @property
    def isDualType(self) -> bool:
        ''' A boolean representing this type's dual-type status. True if it is a dual-type. '''
        raise NotImplementedError
    
    @property
    def firstType(self):
        raise NotImplementedError

    @property
    def secondType(self):
        raise NotImplementedError

    @property
    def offensiveMatchupData(self) -> dict:
        ''' Returns this type's offensive matchup data. '''
        return self.matchupData["offensive"]

    @property
    def defensiveMatchupData(self) -> dict:
        ''' Returns this type's defensive matchup data. '''
        return self.matchupData["defensive"]

    def getMultipliers(self, typeName:str) -> tuple:
        ''' Gets offensive and defensive multipliers this type has in relation to the given type's name.

        @return: Returns a tuple containing two floats which represent the offensive and defensive multipliers respectively.
        '''
        offensiveMultiplier, defensiveMultiplier = None, None
        for (multiplier_str, names) in self.offensiveMatchupData.items():
            if typeName in names:
                offensiveMultiplier = float(multiplier_str)
                break
        for (multiplier_str, names) in self.defensiveMatchupData.items():
            if typeName in names:
                defensiveMultiplier = float(multiplier_str)
                break
        return (offensiveMultiplier, defensiveMultiplier)


    def validate(self) -> None:
        ''' Validates this MatchupManager.
        
        @raise ValidationError: If this MatchupManager isn't valid
        
        '''
        offensiveMatchups = list(chain(*self.offensiveMatchupData.values()))
        defensiveMatchups = list(chain(*self.defensiveMatchupData.values()))

        for matchup in offensiveMatchups:
            count = defensiveMatchups.count(matchup)
            if count == 0:
                raise ValidationError("\"{1}\" doesn't exist in \"{0}\" defensive matchup data.".format(self.name, matchup))
            elif count > 1:
                raise ValidationError("\"{1}\" exists in multiple locations in \"{0}\" defensive matchup data.".format(self.name, matchup))
        for matchup in defensiveMatchups:
            count = offensiveMatchups.count(matchup)
            if count == 0:
                raise ValidationError("\"{1}\" doesn't exist in \"{0}\" offensive matchup data.".format(self.name, matchup))
            elif count > 1:
                raise ValidationError("\"{1}\" exists in multiple locations in \"{0}\" offensive matchup data.".format(self.name, matchup))

    def rate(self, *args, **kwargs) -> tuple:
        ''' Rates this MatchupManager instance. Subclasses may overload this function. 

        @param weights A tuple that contains 2 callables that take in a float representing the multiplier and output a float representing the corresponding weight.
        The first callable is the offensive weight function and the second is the defensive weight function.

        @raise ValidationError: If this MatchupManager isn't valid.

        @returns Returns a tuple containing the offensive rating and defensive rating.
        
        '''

        self.validate() # Make sure this instance is valid

        # Getting the weight functions from the keywords parameter
        offensiveWeightFunc, defensiveWeightFunc = kwargs["weights"] if "weights" in kwargs.keys() else MatchupManager.defaultWeights()

        # Compiling a list of all the type names
        allTypeNames = []
        for typeNames in self.offensiveMatchupData.values():
            allTypeNames += typeNames

        offensiveScore = 0
        defensiveScore = 0

        # Iterating through all the type names and evaluating their matchup relationship with the current MatchupManager.
        for typeName in allTypeNames:
            offensiveMultiplier, defensiveMultiplier = self.getMultipliers(typeName)
            offensiveWeight, defensiveWeight = offensiveWeightFunc(offensiveMultiplier), defensiveWeightFunc(defensiveMultiplier)
            
            base_score = 1

            offensiveScore += base_score * offensiveWeight
            defensiveScore += base_score * defensiveWeight

        return (offensiveScore, defensiveScore)

    def display(self) -> None:
        ''' Displays a primitive visual representation of this object's matchup data. This is just for convenience.'''
        root = Tk()
        root.title(self.name)
        root.configure(background="white")

        colors = MatchupManager.colors() # Load the colors

        # Creating the title label
        titleLabel = Label(root, text=self.name, background="white")
        titleLabel.grid(row=0, column=0, columnspan=5) # This will span the entire grid

        def createMatchupDataLabels(items:list, columns:tuple):
            ''' A generalized function that creates tkinter labels and places them in their designated rows. '''
            rowNumber = 2
            for (multiplier_str, typeNames) in items:
                if len(typeNames) == 0:
                    continue

                multiplierLabel = Label(root, text=multiplier_str, background="white")
                multiplierLabel.grid(row=rowNumber, column=columns[0], rowspan=len(typeNames), sticky=NW)

                for typeName in typeNames:
                    lbl = Label(root, text=typeName, background=colors[typeName])
                    lbl.grid(row=rowNumber, column=columns[1])
                    rowNumber += 1

        # Offensive Data
        offensiveTitleLabel = Label(root, text="Offensive", background="white")
        offensiveTitleLabel.grid(row=1, column=0, columnspan=2, sticky=N)

        createMatchupDataLabels(sorted(self.offensiveMatchupData.items(), key=lambda item: float(item[0]), reverse=True), (0,1))      
        
        # Defensive Data
        defensiveTitleLabel = Label(root, text="Defensive", background="white")
        defensiveTitleLabel.grid(row=1, column=3, columnspan=2, sticky=N)

        createMatchupDataLabels(sorted(self.defensiveMatchupData.items(), key=lambda item: float(item[0])), (3,4))
        
        # Displaying the window
        root.mainloop()
