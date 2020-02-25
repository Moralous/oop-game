from character import Character
from room_definitions import *

# Damage types:
# 0 = blunt
# 1 = bladed
# 2 = ranged
# 3 = magic

# Character(name, capacity, attack_speech, health, weapon, resistance, weakness, home room)

ghoul = Character(name="Ghoul",capacity=10,speech="The ghoul screams.",
                  attack_speech="The ghoul screeches and swings at you!",
                  health=4,resistance=0,weakness=1,starting_room=central_hallway,equipped_weapon=claws)
central_hallway.enemy = ghoul

haunted_kitchenware = Character(name="Chef's Apparition",capacity=10,
                                speech="The presence of a long-dead cook reigns over this kitchen.",
                                attack_speech="The blades slice through the air towards you",
                                health=6,equipped_weapon=hovering_knives,resistance=2,weakness=3,
                                starting_room=kitchen)
kitchen.enemy = haunted_kitchenware

animated_armour = Character(name="Animated Armour",speech="The Animated Armour remains silent. It's unsettling...",
                            capacity=10,attack_speech="The Animated Armour says nothing as it lunges towards you."
                            ,health=15,equipped_weapon=gauntlets,
                            resistance=1,weakness=0,starting_room=western_hallway)
western_hallway.enemy=animated_armour