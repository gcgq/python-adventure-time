import random

class Room(object):
    def __init__(self, exits=["hallway"]):
        self.items = []
        self.exits = exits

class House(object):
    def __init__(self):
        self.rooms = {"bedroom": Room(),
                    "bathroom": Room(),
                    "storage room": Room(),
                    "kitchen": Room(),
                    "dining room": Room(),
                    "hallway": Room(["bedroom",
                                    "bathroom",
                                    "kitchen",
                                    "entrance",
                                    "storage room",
                                    "dining room"]),
                    "entrance": Room()}

        self.place_item("eggs")
        self.place_item("basket")

    def place_item(self, item):
        rms = list(self.rooms.keys())
        place = random.choice(rms)
        if place not in ["hallway", "entrance"]:
            self.rooms[place].items.append(item)
        else:
            self.place_item(item)

class Player(object):
    def __init__(self):
        self.location = "entrance"
        self.items = []
        self.escaped = False

    def move(self, loc):
        exits = loc.rooms[self.location].exits
        destination = ""
        while destination not in exits:
            print("Nearby rooms:", exits)
            destination = input("Move where? ").lower()
            if destination not in exits:
                print("{} can't be reached from the {}.".format( destination, self.location ))
            else:
                self.location = destination
                print("You move to the {}.".format( destination ))

    def get_item(self, loc):
        item = input("Get what? ").lower()
        if item in loc.rooms[self.location].items:
            if item=="eggs" and "basket" not in self.items:
                print("Get a basket, dude.")
            else:
                print("You got the {}!".format(item))
                self.items.append(item)
                loc.rooms[self.location].items.remove(item)
        else:
            print("I don't see the {} anywhere.".format(item))

def menu(player, house):
    print(("1) MOVE       2) LOOK\n"
           "3) GET item   4) check INVENTORY\n"))

    menu_choice = input("Enter command: ").lower()

    if menu_choice in ("1","m","move"):
        player.move(house)
    elif menu_choice in ("2","l","look"):
        print("Nearby rooms:", house.rooms[player.location].exits)
        print("Items in this room:", house.rooms[player.location].items)
    elif menu_choice in ("3","g","get"):
        player.get_item(house)
    elif menu_choice in ("4","i","inventory"):
        print("Items in inventory:", player.items)
    else:
        print("Unknown. Try again")


def start():
    player = Player()
    house = House()
    print(("Adventure Time\n\n"
        "The objective is to find eggs (you need a basket to hold them, though), "
        "and return to the entrance.\n"
    ))
    while( player.escaped == False ):
        print("\nYour current location is the {}".format(player.location))
        if player.location == "entrance" and "eggs" in player.items:
            player.escaped = True
            print("Congratulations! You entered a house that isn't yours and took some eggs!")
        else:
            menu(player, house)

start()
