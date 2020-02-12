from time import sleep
from sys import stdout

class Character():
    def __init__(self, name, capacity):
        self.name = name
        self.health = 10
        self.capacity = capacity

    def __repr__(self):
        return "Character(\"{}\")".format(self.name)

    def set_description(self, description):
        self.description = description

    def set_speech(self, speech):
        self.speech = speech

    def speak(self):
        if self.speech:
            print("{}: {}".format(self.name, self.speech))
        else:
            print("{} says nothing...".format(self.name))

    def death_animation(self):
        print("\r\n\n\n")
        print("\r o\n/|\\\n.|.\n\n\n")
        print("\r o\n/|\n_>\n\n\n")
        print("\r>->o\n    \- \"I am dead now...\"\n\n\n")


class Player(Character):
    def __init__(self, name, starting_room):
        super().__init__(name)
        self.room = starting_room

    def move(self, room):
        self.room = room


class Enemy(Character):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
