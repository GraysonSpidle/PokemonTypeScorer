from errors import ValidationError

class StatsManager:
    def __init__(self, hp:int=1, attack:int=1, defense:int=1, special_attack:int=1, special_defense:int=1, speed:int=1, **kwargs):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    @property
    def stats(self) -> tuple:
        return (self.hp, self.attack, self.defense, self.special_attack, self.special_defense, self.speed)

    def validate(self):
        for stat in self.stats:
            if stat <= 0:
                raise ValidationError("A StatsManager's stat cannot be 0.")
