class Event():
    def __init__(name:str,activation_string:str):
        self.name = name
        self.activation_string = activation_string


class HealEvent(Event):
    def __init__(name:str,activation_string:str,heal_amount:int=3):
        super().__init__(name, activation_string)
        self.heal_amount = heal_amount

    def activate(self, target):
        target.health += self.heal_amount
        if target.health > target.