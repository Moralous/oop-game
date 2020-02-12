import rooms
from character import Player, Enemy
from random import choice
from utilities import slow_print
from time import sleep

random_characters = "@#~`¬/‡†☼¶┼╞╟╚╔╩╦╠╬╧§#$%αßπΣΦΘΩδµτε∩⌠⌡¿þ\\"

control_string = "\nOptions:\nhelp - displays this message\
\nmove [room name] - move to an adjacent room\
\nattack - attack the nearest enemy\
\nuse [item name] - use an item\
\ninventory - list your available items\n"

break_string = "################################################"

running = True
last_sentence = ""


def handleInput(control):
    """Handles a command. Returns True if the command is legal"""
    if control == "end":
        global running
        running = False
        return True
    elif control == "help":
        return False
    elif control[0:5].lower() == "move ":
        room = None
        destination = control[5:].lower()
        current_room = player.room
        linked_rooms = current_room.get_linked_rooms()
        for r in linked_rooms:
            if r[0].name.lower() == destination:
                room = r[0]
        if room is None:
            print("INVALID ROOM")
            return False
        else:
            player.move(room)
            return True
    else:
        print("INVALID COMMAND")
        return False

player = Player(input("What is your name, adventurer?:\n>"),
                10,
                rooms.outside)

if player.name == "debug":
    running = False

if running:
    sleep(1)
    print("Ah...")
    sleep(2)
    print("{}...".format(player.name))
    sleep(4)
    print("Good luck...")
    sleep(2)
    print("\n"*100)

##string = ""
##for i in range(50):
##    string += "\n"
##    for n in range(100):
##        string += choice(random_characters)
##print(string)

print("\n"*4)

while running:
    last_sentence = player.room.on_enter()
    print(last_sentence)
    while handleInput(input(">")) == False:
        print(break_string)
        print(control_string)
        print(break_string)
        print(last_sentence)
    print(break_string)
