from sys import stdout

directions = ["North", "East", "South", "West"]
link_table = [2, 3, 0, 1]

class Room():
    def __init__(self,room_name:str, init_desc:str, desc:str, you_move:str,
                 enemy=None, item=None, room_art:str=""):
        """Room(Room name, initial entrance description, secondary entrance description,\
         generic movement script)"""
        self.name = room_name
        self.linked_rooms = []
        self.character = None
        self.init_desc = init_desc
        self.desc = desc
        self.visited = False
        self.you_move = you_move
        self.enemy = enemy
        self.item = item
        self.room_art = room_art

    def __repr__(self):
        variables = vars(self)
        string = "Room("
        for key, value in variables.items():
            if type(value) == str:
                string += "{}=\"{}\",".format(key, value)
            else:
                string += "{}={},".format(key, value)
        string = string[:-1]
        string += ")"
        return string

    def on_enter(self):
        print(self.room_art)
        print(self.you_move)
        string = self.init_desc if not self.visited else self.desc
        self.visited = True
        string += "\n{}".format(self.print_movements())
        return string, False if self.enemy is None else True

    def link_room(self, room_to_link, direction):
        """Links room_to_link to this room. Directions
0, 1, 2, 3 are North, East, South, West respectively"""
        self.linked_rooms.append((room_to_link, direction))
        room_to_link.linked_rooms.append((self, link_table[direction]))

    def get_linked_rooms(self):
        return self.linked_rooms

    def print_movements(self):
        string = "\n"
        for room in self.linked_rooms:
            string += "The {} lies to the {}...\n".format(room[0].name,
                                                    directions[room[1]])
        return string

    def set_character(self, character_name):
        self.character = character_name

    def get_character(self):
        return self.character
