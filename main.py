from room_definitions import *
from enemy_definitions import *
from weapon_definitions import *
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
last_sentence = ""
in_combat = False
enemies_remaining = 3
player = Character(input("What is your name, adventurer?:\n>"), starting_room=outside)


def clear():
    print("\n"*100)


def handle_input(control):
    """Handles a command.
    Returns 0 if the command is illegal or "help".
    Returns 1 for move
    Returns 2 for attack
    Returns 3 for use
    Returns 4 for inventory
    Returns 5 for die"""
    if control.lower() == "die":
        global alive
        alive = False
        return 5
    elif control.lower() == "help":
        return 0
    elif control[0:5].lower() == "move ":
            destination = control[5:].lower()
            return handle_move(destination)
    elif control.lower() == "attack":
        if not in_combat:
            print("You swing your {} at thin air...".format(player.equipped_weapon.name.lower()))
        return 2
    elif control[0:4].lower() == "use ":
        item_name = control[4:].lower()
        item = None
        for i in player.inventory:
            if i.name.lower() == item_name:
                item = i
        if item is not None:
            item.use(player)
            return 3
        else:
            print("You search your pockets but cannot find {}...".format(item_name))
            return 0
    elif control[0:9].lower() == "inventory":
        player.print_inventory()
        return 4
    else:
        print("INVALID COMMAND")
        return 0


def handle_move(destination):
    room = None
    current_room = player.room
    linked_rooms = current_room.get_linked_rooms()
    for r in linked_rooms:
        if r[0].name.lower() == destination:
            room = r[0]
    if room is None:
        print("INVALID ROOM")
        print(player.room.print_movements())
        return 0
    else:
        player.move(room)
        return 1


def combat_loop():
    enemy = player.room.enemy
    while enemy.health > 0:
        print("The {} swipes at you with its {}.".format(enemy.name, enemy.equipped_weapon.name))
        enemy.attack(player)
        if player.health <= 0:
            break

        action = handle_input(input(">"))
        while action == 0:
            print(break_string)
            print(control_string)
            print(break_string)
            action = handle_input(input(">"))
        if action == 1:
            print("The {} gets a glancing blow as you exit the room.".format(enemy.name))
            print("You lose 1 health.{}".format("" if player.health <= 0 else
                                                " You have {} health remaining...".format(player.health)))
        elif action == 2:
            print("You swipe at {} with your {}".format(enemy.name, player.equipped_weapon.name))
            player.attack(enemy)
            if enemy.health <= 0:
                global enemies_remaining
                enemies_remaining -= 1
                player.room.enemy = None
                print("The {} falls dead to the ground.".format(enemy.name))
                print("There are now {} enemies remaining...".format(enemies_remaining))
                break






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
    last_sentence, in_combat = player.room.on_enter()
    print(last_sentence)
    if player.room.item is not None:
        print("!!!!!\nYou find a {}, and pick it up.".format(player.room.item.name))
        player.pick_up(item=player.room.item)
        player.room.item = None
    if in_combat:
        enemy = player.room.enemy
        print("COMBAT HAS BEGUN WITH {}".format(enemy.name.upper()))
        enemy.speak()
        combat_loop()
        if player.health <= 0:  # Handles player death
            alive = False
            print("The world fades from view, and the last thing you see is the floor rushing towards your head...\
            \n You have Died...")

    while handle_input(input(">")) == 0:  # As long as the player is dumb and inputs invalid commands, do not advance
        print(break_string)
        print(control_string)
        print(break_string)
        print(last_sentence)

    print(break_string)
