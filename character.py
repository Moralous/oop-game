from room import Room
from weapons import unarmed
from item import Weapon
from math import floor
from random import randrange

damage_types = [
    "blunt",
    "bladed",
    "ranged",
    "magic"
]

class Character():
    def __init__(self, name:str, capacity:int, speech:str=""):
        self.name = name
        self.health = 10
        self.capacity = capacity
        self.equipped_item = unarmed
        self.resistance = None
        self.weakness = None
        self.speech = speech

    def __repr__(self):
        return "Character(\"{}\")".format(self.name)

    def speak(self):
        if self.speech:
            print("{}: {}".format(self.name, self.speech))
        else:
            print("{} says nothing...".format(self.name))

    def take_damage(self, dmg:int, dmg_type:int):
        """Handles weaknesses, resistances, and feedback. Returns True if the attack \
        kills the character"""
        if dmg_type == self.weakness:
            print("{} is weak to {}. Double damage!".format(self.name, damage_types[dmg_type]))
            dmg = floor(dmg/2)
        elif dmg_type == self.resistance:
            print("{} is resistant to {}. Half damage!".format(self.name, damage_types[dmg_type]))
            dmg = floor(dmg/2)
        self.health -= dmg
        print("{} took {} damage.".format(self.name, str(dmg)))
        return True if self.health <= 0 else False

    def attack(self, target:'Character', weapon:Weapon):
        """Instructs this character object to attack the target character with weapon."""
        dmg = weapon.damage
        dmg_type = weapon.dmg_type
        if target.health <= 0:
            print("{} is already dead!".format(target.name))
            return False
        else:
            if randrange(0, 100) <= weapon.hit_chance:
                dmg = weapon.dmg + randrange(-1, 1)
                print("Hit!")
                target.take_damage(dmg, weapon.dmg_type)


    def death_animation(self):
        print("\r\n\n\n")
        print("\r o\n/|\\\n.|.\n\n\n")
        print("\r o\n/|\n_>\n\n\n")
        print("\r>->o\n    \- \"I am dead now...\"\n\n\n")


class Player(Character):
    def __init__(self, name:str, capacity:int, starting_room:Room):
        super().__init__(name, capacity)
        self.room = starting_room

    def move(self, room:Room):
        self.room = room


class Enemy(Character):
    def __init__(self, name:str, capacity:int, room:Room):
        super().__init__(name, capacity)
        self.room = room
