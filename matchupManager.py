from tkinter import Tk, Label, Y, N, LEFT, RIGHT, TOP, Grid, N, NW
import json

class MatchupManager:
    ''' This is the class that manages Matchups (wow). It's primary use is to serve as an abstract class
    to provide the framework needed to rate types and Pokemon based on their type matchups. In essence, this
    class encapsulates a number of dictionaries and provides a standard way of accessing them. It also
    adds some convenience methods.

    The dictionary that each instance contain are structured as follows:
        key : str
            The key is either "offensive" or "defensive".
        value : dict
            Another dict of multipliers and a list PokemonType names.
    
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
        offensiveMultiplier, defensiveMultiplier = None, None
        for (multiplier, names) in self.offensiveMatchupData.items():
            if typeName in names:
                offensiveMultiplier = multiplier
                break
        for (multiplier, names) in self.defensiveMatchupData.items():
            if typeName in names:
                defensiveMultiplier = multiplier
                break
        return (offensiveMultiplier, defensiveMultiplier)


    def validate(self) -> None:
        ''' Validates this MatchupManager
        It checks the current matchup data is valid.
        
        Raises
        ------

        Exception : This will be raised if there is an error in the matchup json file. 
            - When a type does exist in the offensive matchup data but doesn't exist in the defensive matchup data and vice versa.
            - When a type exists in multiple locations in either the offensive or defensive matchup data.
        
        '''
        offensiveMatchups = []
        for matchup_list in self.offensiveMatchupData.values():
            offensiveMatchups += matchup_list
        defensiveMatchups = []
        for matchup_list in self.defensiveMatchupData.values():
            defensiveMatchups += matchup_list

        for matchup in offensiveMatchups:
            count = defensiveMatchups.count(matchup)
            if count == 0:
                raise Exception("Invalid MatchupManager ({0}): {1} doesn't exist in the defensive matchups.".format(self.name, matchup))
            elif count > 1:
                raise Exception("Invalid MatchupManager ({0}): {1} exists in multiple locations in the defensive matchups.".format(self.name, matchup))
        for matchup in defensiveMatchups:
            count = offensiveMatchups.count(matchup)
            if count == 0:
                raise Exception("Invalid MatchupManager ({0}): {1} doesn't exist in the offensive matchups.".format(self.name, matchup))
            elif count > 1:
                raise Exception("Invalid MatchupManager ({0}): {1} exists in multiple locations in the offensive matchups.".format(self.name, matchup))

    def rate(self, *args, **kwargs) -> float:
        self.validate()
        offensiveWeightFunc, defensiveWeightFunc = kwargs["weights"] if "weights" in kwargs.keys() else MatchupManager.defaultWeights()
        allTypeNames = []
        for typeNames in self.offensiveMatchupData.values():
            allTypeNames += typeNames
        numOfTypes = len(allTypeNames)

        output = 0

        for typeName in allTypeNames:
            offensiveMultiplier, defensiveMultiplier = self.getMultipliers(typeName)
            offensiveWeight, defensiveWeight = offensiveWeightFunc(offensiveMultiplier), defensiveWeightFunc(defensiveMultiplier)
            
            if offensiveMultiplier == '0.0':
                output += offensiveWeight * 0.25
            else:
                output += offensiveWeight * 0.25 + (1/float(offensiveMultiplier)) * (1 / numOfTypes)
            output += defensiveWeight * 0.25 + (float(defensiveMultiplier) * (1 / numOfTypes))

        return output

    def display(self) -> None:
        ''' Displays a primitive visual representation of this object's matchup data. '''
        root = Tk()
        root.title(self.name)
        root.configure(background="white")

        colors = MatchupManager.colors() # Load the colors

        titleLabel = Label(root, text=self.name, background="white")
        titleLabel.grid(row=0, column=0, columnspan=5)

        def createMatchupDataLabels(items:list, columns:tuple):
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

        offensiveTitleLabel = Label(root, text="Offensive", background="white")
        offensiveTitleLabel.grid(row=1, column=0, columnspan=2, sticky=N)

        createMatchupDataLabels(sorted(self.offensiveMatchupData.items(), key=lambda item: float(item[0]), reverse=True), (0,1))      
        
        defensiveTitleLabel = Label(root, text="Defensive", background="white")
        defensiveTitleLabel.grid(row=1, column=3, columnspan=2, sticky=N)

        createMatchupDataLabels(sorted(self.defensiveMatchupData.items(), key=lambda item: float(item[0])), (3,4))
        
        root.mainloop()