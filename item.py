class Item():
    def __init__(self, name, description, weight):
        """An item a character can use. Weight should be 1, 2, or 3 for\
 light, average, and heavy respectively"""
        self.name = name
        self.description = description
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, description, weight:int=1, dmg, dmg_type,
    hit_chance):
        """Damage types:
0 = blunt
1 = bladed
2 = ranged
3 = magic
"""
        super().__init__(name, description, weight)
        self.damage = dmg
        self.damage_type = dmg_type
        self.hit_chance = hit_chance

    def use(self, target):
        print("You equip the {}.".format(self.name))
        target.equipped_weapon = self


class Potion(Item):
    def __init__(self, name, description, weight:int=1, size:int=4,
    use_text:str=""):
        super().__init__(name, description, weight)
        self.size = size
        self.use_text = use_text

    def use(self, target):
        item_index = target.inventory.index(self)
        target.inventory.pop(item_index)
        print("You drink the potion and gain {} health...".format(self.size))
        target.heal(self.size)

