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
unarmed = Weapon("Fists", "Your bare hands.", 0, 1, 0, 80)
cane = Weapon("Cane", "A gentlemen's walking aid.", 2, 2, 0, 90)
sword = Weapon("Longsword", "Ceremonial and unwieldy, but it'll do.", 3, 1, 4, 70)
pocket_knife = Weapon("Pocket Knife", "Likely used for whittling, but you won't have the time. Quite short.",
                      1, 2, 1, 65)

# Enemy-only weapons
# A weight of -1 implies that they *cannot* be picked up the player
claws = Weapon("Claws", "They look sharp and terrifying.", -1, 2, 1, 65)
hovering_knives = Weapon("Hovering Knives", "They spin and slice through the air.", -1, 3, 3, 80)