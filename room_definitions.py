from room import Room
from item import *
from weapon_definitions import *

cloakroom = Room("cloakroom",
                "The door slams closed behind you, shutting out the sound \
of the storm. Water drips off you onto the welcome mat.",
                "The storm continues to rage on outside; the sound of \
the rain and lightning is almost calming.",
                "You step into the dusty cloakroom.",
                 item=Potion(name="Tonic",description="Supposedly good for your health.",weight=1,size=3))

outside = Room("Outside",
               "You're hopelessly lost and the storm continues around you. \
That mansion looks rather cosy in comparison.",
               "There's nothing out here...",
               "You step out into the pouring rain")

central_hallway = Room("Central Hallway",
                       "The hallway is lined with portraits of faces you don't \
recognise.",
                       "You feel like something's watching you...",
                       "You step into the hallway",
                       item=pocket_knife)

courtyard = Room("Courtyard",
                 "The rain pelts down on you out here, and the soil in the \
borders has begun to flood onto the paving. The bloodstains do not smudge.",
                 "It's a beautiful sight, ruined by the bloodstains...",
                 "You open the sliding doors and step into the open-roof \
courtyard", item=sword)

western_hallway = Room("Western Hallway",
                       "Light shines through the large stained glass windows \
faintly colouring the hallway, and provide what should be a lovely view into \
the courtyard.",
                       "You can't see the blood through the red glass...",
                       "The door creaks open and you step into the corridor",
                       item=cane)

servants_quarters = Room("Servant's Quarters",
                         "Several bunk beds remain unmade, as if the sheets \
had been thrown off in a rush.",
                         "Are those claw marks on the bed panels?",
                         "The door opens silently, clearly well oiled",
                         item=Potion(name="Large Tonic", description="Supposedly even better for your health.", weight=1, size=10))

kitchen = Room("Kitchen",
               "Flies buzz around rotting food and blood stains the white-tiled floor.",
               "You hope the blood isn't human...",
               "The stench hits you as soon as you cross the threshold",
               item=Potion(name="Dusty Potion", description="You can't seem to clear the label", weight=1, size=4))

dining_room = Room(room_name="Dining Room",init_desc="The food here would have looked delectable.",
                   desc="Your stomach rumbles...",
                   you_move="The smell of rot fills your nostrils")

outside.link_room(cloakroom, 0)
cloakroom.link_room(central_hallway, 0)
central_hallway.link_room(courtyard, 3)
central_hallway.link_room(western_hallway, 3)
central_hallway.link_room(servants_quarters, 1)
servants_quarters.link_room(kitchen, 1)
