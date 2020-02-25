class Item():
    def __init__(self, name, description, weight):
        """An item a character can use. Weight should be 1, 2, or 3 for\
 light, average, and heavy respectively"""
        self.name = name
        self.description = description
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, description, weight, dmg, dmg_type, hit_chance):
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

    def use(self, player):
        print("You equip the {}.".format(self.name))
        player.equipped_weapon = self


class Potion(Item):
    def __init__(self, name, description, weight, size):
        super().__init__(name, description, weight)
        self.size = size

    def use(self, player):
        item_index = player.inventory.index(self)
        player.inventory.pop(item_index)
        print("You drink the potion and gain {} health...".format(self.size))
        player.health += self.size
        if player.health >= 10:
            player.health = 10
            print("You're back to full health.")
        else:
            print("You're now at {} health".format(player.health))

