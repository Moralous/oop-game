from item import Weapon

# Damage types:
# 0 = blunt
# 1 = bladed
# 2 = ranged
# 3 = magic

# Weapon(name, description, weight, damage, damage type, hit chance)
# Description is standalone
# Hit chance is an integer between 0 and 100, which represents the percentage chance of a an attack hitting

# Player equipable weapons:
unarmed = Weapon(name="Fists",description="Your bare hands.",weight=0,dmg=1,dmg_type=0,hit_chance=80)
cane = Weapon(name="Cane",description="A gentlemen's walking aid.",weight=2,dmg=2,dmg_type=0,hit_chance=90)
sword = Weapon(name="Longsword",description="Ceremonial and unwieldy, but it'll do.",weight=3,dmg=4,hit_chance=70,
               dmg_type=1)
pocket_knife = Weapon(name="Pocket Knife",description="Likely used for whittling, but you won't have the time.\
 Quite short.",
                      weight=1,dmg=4,dmg_type=1,hit_chance=65)

# Enemy-only weapons
# A weight of -1 implies that they *cannot* be picked up the player
claws = Weapon(name="Claws",description="They look sharp and terrifying.",weight=-1,dmg=2,dmg_type=1,hit_chance=65)
hovering_knives = Weapon(name="Hovering Knives",description="They spin and slice through the air.",weight=-1,
                         dmg=3,dmg_type=1,hit_chance=80)
gauntlets = Weapon(name="Steel Gauntlets",description="Pack a real punch.",weight=-1,dmg=3,dmg_type=0,hit_chance=80)