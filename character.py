from room import Room
from room_definitions import outside
from weapon_definitions import unarmed
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
    def __init__(self, name:str, capacity:int=10, speech:str="", health:int=10,
                 equipped_weapon:Weapon=unarmed, resistance:int=None, weakness:int=None,
                 starting_room:Room=outside, attack_speech:str=None):
        self.name = name
        self.capacity = capacity
        self.speech = speech
        self.health = health
        self.equipped_weapon = equipped_weapon
        self.resistance = resistance
        self.weakness = weakness
        self.room = starting_room
        self.attack_speech = attack_speech

        self.inventory = []

    def __repr__(self):
        return "Character(\"{}\")".format(self.name)

    def speak(self):
        if self.speech:
            print(self.speech)
        else:
            print("{} says nothing.".format(self.name))

    def move(self, room:Room):
        self.room = room

    def take_damage(self, dmg:int, dmg_type:int):
        """Handles weaknesses, resistances, and feedback. Returns True if the attack \
        kills the character"""
        dmg = 1 if dmg == 0 else dmg
        if dmg_type == self.weakness:
            print("{} is weak to {}. Double damage!".format(self.name, damage_types[dmg_type]))
            dmg = floor(dmg*2)
        elif dmg_type == self.resistance:
            print("{} is resistant to {}. Half damage!".format(self.name, damage_types[dmg_type]))
            dmg = floor(dmg/2)
        dmg = 1 if dmg == 0 else dmg
        self.health -= dmg
        print("{} took {} damage.".format(self.name, str(dmg)))
        print("{} has {} health remaining".format(self.name, self.health))
        return True if self.health <= 0 else False

    def attack(self, target:'Character'):
        """Instructs this character object to attack the target character with weapon."""
        print(self.attack_speech)
        weapon = self.equipped_weapon
        dmg = weapon.damage
        dmg_type = weapon.damage_type
        if target.health <= 0:
            print("{} is already dead!".format(target.name))
            return False
        else:
            if randrange(0, 100) <= weapon.hit_chance:
                dmg = weapon.damage + randrange(-1, 1)
                print("Hit!")
                target.take_damage(dmg, weapon.damage_type)
                return True
            else:
                print("Miss!")
                return False

    def pick_up(self, item):
        print("You slip {} into your knapsack.".format(item.name))
        self.inventory.append(item)

    def print_inventory(self):
        print("You take a moment to look through your bag:")
        if len(self.inventory) == 0:
            print("There's nothing there!")
        for item in self.inventory:
            if not item == self.equipped_weapon:
               print("{} - {}".format(item.name, item.description))

    def death_animation(self):
        print("\r\n\n\n")
        print("\r o\n/|\\\n.|.\n\n\n")
        print("\r o\n/|\n_>\n\n\n")
        print("\r>->o\n    \- \"I am dead now...\"\n\n\n")