from room import *
from random import randrange

# generate a number of rooms
# link them in an interesting way
# Add The Final Room to the end
names = ["Dungeon Room"]


def generate_rooms(dungeon_length:int=5) -> Room:
    first_room = Room(room_name="The First Room",init_desc="You begin your \
    journey through the dungeon.",desc="Where it all begins...",
    you_enter="You step into the first room")


def random_name():
    return names[randrange(0, len(names)-1)]