import random

class Room(object):
    def __init__(self, name, adjacent_rooms=["hallway"]):
        self.name = name
        self.items = []
        self.adjacent_rooms = adjacent_rooms

    def room_adjacent(self, next_room):
        if next_room in self.adjacent_rooms:
            return True
        else:
            return False

    def get_name(self):
        return self.name

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def check_item(self, item):
        if item in self.items:
            return True
        else:
            return False

    def search(self):
        print(self.items)

class House(object):
    def __init__(self):
        self.rooms = {"bedroom": Room("bedroom"),
                    "bathroom": Room("bathroom"),
                    "storage room": Room("storage room"),
                    "kitchen": Room("kitchen"),
                    "dining room": Room("dining room"),
                    "hallway": Room("hallway", ["bedroom",
                                    "bathroom",
                                    "kitchen",
                                    "entrance",
                                    "storage room",
                                    "dining room"]),
                    "entrance": Room("entrance")}

        self.rooms_list = list(self.rooms.keys())
        self.place_item("basket")
        self.place_item("eggs")

    def place_item(self, item):
        place = random.choice(self.rooms_list)
        if place not in ["hallway", "entrance"]:
            self.rooms[place].add_item(item)
        else:
            self.place_item(item)

    def get_room(self, name):
        return self.rooms[name]

class Player(object):
    def __init__(self, house):
        self.house = house
        self.location = self.house.get_room("entrance")
        self.items = []
        self.escaped = False

    def move(self, next_room):
        if self.location.room_adjacent(next_room):
            self.location = self.house.get_room(next_room)
        else:
            print("You can't go there from here!")

    def search(self):
        self.location.search()

    def check_bag(self):
        print(self.items)

    def pick_up(self, item):
        if item == "eggs":
            if "basket" not in self.items:
                print("You can't pick anything up without a basket!")
            else:
                if self.location.check_item(item):
                    self.items.append(item)
                    self.location.remove_item(item)
                    print(item, " picked up!")
                else:
                    print("That item is not here!")
        else:
            if self.location.check_item(item):
                self.items.append(item)
                self.location.remove_item(item)
                print(item, "picked up!")
            else:
                print("That item is not here!")

    def exit(self):
        if self.location == self.house.get_room("entrance"):
            if "eggs" in self.items:
                print("You have escaped!")
                self.escaped = True
            else:
                print("You don't have the balls, I mean, eggs, to leave here!")
        else:
            print("You can't leave from here! Bahahaha!")

    def escape_check(self):
        return self.escaped

def start():
    house = House()
    player = Player(house)

    def menu():
        print("Current Location:", player.location.get_name())

        action_list = {"move to hallway": [player.move, "hallway"],
                       "move to bedroom": [player.move, "bedroom"],
                       "move to bathroom": [player.move, "bathroom"],
                       "move to kitchen": [player.move, "kitchen"],
                       "move to entrance": [player.move, "entrance"],
                       "move to storage room": [player.move, "storage room"],
                       "move to dining room": [player.move, "dining room"],
                       "search": [player.search],
                       "check bag": [player.check_bag],
                       "pick up basket": [player.pick_up, "basket"],
                       "pick up eggs": [player.pick_up, "eggs"],
                       "exit": [player.exit]}
        action = input("What would you like to do? Options: move to (room), search, pick up (item), check bag, exit ")

        if action in action_list.keys():
            if len(action_list[action]) > 1:
                action_list[action][0](action_list[action][1])
            else:
                action_list[action][0]()
        else:
            print("That is not a valid action. Please try again.")

    while player.escape_check() == False:
        menu()

start()
