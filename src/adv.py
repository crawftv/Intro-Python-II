from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]


# add items to room
items = {"chekovs_gun": Item("chekovs_gun", "must be used by the end of the game")}
room["outside"].items[items["chekovs_gun"].name] =  items["chekovs_gun"]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
direction_map = {
    "n": "n_to",
    "s": "s_to",
    "e": "e_to",
    "w": "w_to",
}
take_synonyms = ["take", "get"]
drop_synonyms = ["drop"]

def take_item(item:str,p:Player):
    try:
        p.items[item] =p.current_room.items[item]
        del p.current_room.items[item]
        items[item].on_take()
    except:
        print("cannot add item to inventory")
        
def drop_item(item:str,p:Player):
    try:
        p.current_room.items[item] = p.items[item]
        del p.items[item]
        items[item].on_drop()
    except:
        print("Cannot drop that item")


def play():
    p = Player(room["outside"])
    while True:
        print(f"\n\nYou are in {p.current_room}")
        print(p.current_room.description)
        if len(p.current_room.items) == 0:
            print("The room is empty")
        else:
            print(f"The room contains {p.current_room.items}")
        sentence = input("what action will you take?\n")
        t = sentence.split(" ")
        v = t[0]
        try:
            n = t[1]
        except:
            pass
        if len(t) == 1:
            if v in direction_map.keys():
                try:
                    p.current_room = getattr(p.current_room, direction_map[v])
                except:
                    print("error, can't move in that diection")
            elif v == "q":
                return False
            elif v in [ "i","inventory"]:
                print(p.items)
            else:
                print("error, that direction is not allowed")
        elif len(t) == 2:
            if t[0] in take_synonyms:
                take_item(t[1],p)
            elif t[0] in drop_synonyms:
                drop_item(t[1],p)
        else:
            print("invalid command")


# If the user enters "q", quit the game.


if __name__ == "main":
    play()
