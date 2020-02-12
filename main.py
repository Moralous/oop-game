from room_definitions import *
from enemy_definitions import *
from character import Character
from time import sleep

random_characters = "@#~`¬/‡†☼¶┼╞╟╚╔╩╦╠╬╧§#$%αßπΣΦΘΩδµτε∩⌠⌡¿þ\\"

control_string = "\nOptions:\nhelp - displays this message\
\nmove [room name] - move to an adjacent room\
\nattack - attack the nearest enemy\
\nuse [item name] - use an item\
\ninventory - list your available items\n"

break_string = "################################################"

debug = True  # Set to True to skip slow flavour text etc.
alive = True
current_enemy = None
last_sentence = ""
player = Character(input("What is your name, adventurer?:\n>"), starting_room=central_hallway)


def clear():
    print("\n"*100)


def handle_input(control):
    """Handles a command.
    Returns 0 if the command is illegal or "help".
    Returns 1 if the command is legal and no further action needs to be taken.
    Returns 2 if the player chooses to attack"""
    if control.lower() == "die":
        global alive
        alive = False
        return 1
    elif control.lower() == "help":
        return 0
    elif control[0:5].lower() == "move ":
            destination = control[5:].lower()
            return handle_move(destination)
    elif control.lower() == "attack":
        return handle_attack()
    else:
        print("INVALID COMMAND")
        return 0


def handle_move(destination):
    if current_enemy is not None:
        print("If you turn your back you'll die...")
        return 1
    else:
        room = None
        current_room = player.room
        linked_rooms = current_room.get_linked_rooms()
        for r in linked_rooms:
            if r[0].name.lower() == destination:
                room = r[0]
        if room is None:
            print("INVALID ROOM")
            return 0
        else:
            player.move(room)
            return 1


def handle_attack():
    global current_enemy
    print("You swing your {} at the {}.".format(player.equipped_weapon.name, current_enemy.name))
    if current_enemy.health <= 0:
        print("You slay the {}!".format(current_enemy.name))
        end_combat()
    else:
        print("The {} still stands.".format(current_enemy.name))
    return 2


def begin_combat():
    global last_sentence
    last_sentence = ""
    global current_enemy
    current_enemy = player.room.enemy
    print("COMBAT HAS BEGUN WITH {}".format(current_enemy.name.upper()))


def end_combat():
    global current_enemy
    player.room.enemy = None
    current_enemy = None


if player.name == "debug":
    alive = False

if alive and not debug:
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

clear()

while alive:
    if player.health <= 0:  # Handles player death
        alive = False
        print("The world fades from view, and the last thing you see is the floor rushing towards your head...\
        \n You have Died...")
    # Stores the last_sentence so that it can be re-printed without modifying game state
    last_sentence = player.room.on_enter()
    if player.room.enemy is not None: enemy_present = True
    print(last_sentence)
    if enemy_present: begin_combat()

    if current_enemy is not None:
        last_sentence = ""
        current_enemy.speak()
        current_enemy.attack(player)

    while handle_input(input(">")) == 0:  # As long as the player is dumb and inputs invalid commands, do not advance
        print(break_string)
        print(control_string)
        print(break_string)
        print(last_sentence)
    print(break_string)
