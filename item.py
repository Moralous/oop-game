class Item():
    def __init__(self, name, description, weight):
        """An item a character can use. Weight should be 1, 2, or 3 for\
 light, average, and heavy respectively"""
        self.name = name
        self.description = description
        self.weight = weight


class Weapon():
    def __init__(self, name, description, weight, dmg, dmg_type, hit_chance):
        super().__init__(name, description, weight)
        self.dmg = dmg
        self.dmg_type = dmg_type
        self.hit_chance = hit_chance
