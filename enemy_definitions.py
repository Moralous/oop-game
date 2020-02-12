from character import Character
from weapon_definitions import *
from room_definitions import *

# Damage types:
# 0 = blunt
# 1 = bladed
# 2 = ranged
# 3 = magic

# Character(name, capacity, attack_speech, health, weapon, resistance, weakness, home room)

ghoul = Character("Ghoul", 10, "The ghoul screeches and swings at you!", 4, claws, 0, 1, central_hallway)
central_hallway.enemy = ghoul

haunted_kitchenware = Character("Chef's Apparition", 10, "The presence of a long-dead cook reigns over this kitchen.",
                                6, hovering_knives, 2, 3, kitchen)
kitchen.enemy = haunted_kitchenware