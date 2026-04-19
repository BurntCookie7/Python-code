import random, sys

#Variables
current_room = "outside"
master_key = False
attic_key = False
cell_key = False
rock = False
entry_open = False

#Functions
def choose():
    global current_room, Castle, actions
    actions = list(Castle[current_room].keys())
    valid_actions = Castle[current_room]
    print("\nLocation: "+current_room.title())
    choice = input(f"You can do the following actions\n {actions}\n")
    if choice in valid_actions:
        valid_actions[choice]()
    else:
        print(f"{choice} is not a valid option")
        choose()

def start():
    input("To choose a action just type it exactly how it is shown\nQuitting exits the game\nProgress is not saved\npress ENTER to continue")
    print("\nYour sister has been taken by a vampire")

def outside():
    global current_room
    current_room = "outside"
    print("\nYou are outside in front of a castle")
    print("Ahead of you is the entrance to the castle,\naround the castle there is a grate leading to the basement\nthe grate can be pulled away")
    choose()

def center():
    global current_room
    current_room = "center room"
    print("\nYou walk into the center of the castle")
    print("Behind you is the entryway of the castle,\nahead there are stairs leading to the balcony\nto your left is the east hall\n to your right is the west hall")
    choose()

def basement():
    global current_room
    current_room = "basement"
    print("\nAs You are in the basement you are hit with a horrible stench\nits cold and dark")
    print("There is a path outside to your left,\nto your right there is a spiral staircase up to the east hall of the castle,\nin front of you there is a hallway")
    choose()

def entry():
    global current_room, rock, entry_open
    if current_room == "outside":
        if rock == True:
            print("\nWith the rock you manage to break the boards holding the door shut")
            rock = False
            entry_open = True
            choose()
        elif entry_open:
            current_room = "entry"
            entry()
        else:
            current_room = "outside"
            print("\nThe door is boarded shut")
            outside()
    else:
        current_room = "entry"
        print("\nYou step into the entry of the castle\ntheres a vase in the corner\nthere are brick walls to your left and right\nit's cold")
        print("Ahead of you leads to the center room of the castle,\nbehind you is the door exiting the castle")
        choose()

def west_hall():
    global current_room
    current_room = "west hall"
    print("\nYou are in the east hall\nlike the east hall it is dark")
    print("You are facing towards a spiral staircase to the basement,\nabove you is the entrance to the attic,\nbehind you the east hall leads to the center room of the castle")
    choose()

def east_hall():
    global current_room
    current_room = "east hall"
    print("\nYou are in the west hall\nlike the west hall it is dark")
    print("You are facing towards the guest bedroom,\nto your left is the master bedroom,\nbehind you is the center room of the castle")
    choose()

def balcony():
    global current_room
    current_room = "balcony"
    print("\nClimbing up the stairs in the center room you arrive on the balcony,\nthere is a light breeze")
    print("Behind you a set of stairs leads to the center room of the castle")
    choose()

def master_bed():
    global current_room
    if master_key:
        current_room = "master bedroom"
    else:
        current_room = "east hall"
        print("\nIt's locked")
        print("you need to find a key")
    choose()

def guest_bed():
    global current_room
    current_room = "guest bedroom"
    print("\nYou are in the guest bedroom")
    print("There's nothing notable in this room")
    choose()

def attic():
    global current_room
    if attic_key:
        current_room = "attic"
        print("\nThe attic is dusty\nthere is a rug on the floor with a strange bump in the middle")
    else:
        current_room = "west hall"
        print("\nIt's locked")
        print("you need to find a key")
    choose()

def examine_empty(item):
    print(f"\nYou look in the {item}\nthere is nothing")
    choose()

def basement_hall():
    global current_room
    current_room = "basement hall"
    print("\nYou walk through the brick walls of the basement into a slim hallway")
    print("To your left there is a door leading to the cell,\nto your right lies the vampires study")
    choose()

def cell():
    if cell_key:
        print("\nYou are in the cell, inside you finally find your sister\nshe has been saved from the vapire that took her")
        sys.exit("You win!!")
    else:
        print("\nIt's locked")
        print("you need to find a key")
        choose()

def study():
    global current_room
    current_room = "study"
    print("\nYou are in the study,\nits filled with books, there are papers scattered around the desk and floor")
    choose()

def examine_study():
    global master_key
    if master_key:
        print("\nYou already looked here")
        print("you found nothing")
    else:
        print("\nYou check the drawers of the desk, inside one you find a key")
        print("Written on it is, Master bedroom")
        master_key = True
    study()

def look_nothing():
    print("\nLooking around you see nothing of interest")
    choose()

def look_master():
    global attic_key
    if attic_key:
        look_nothing()
    else:
        print("\nSitting on a nightstand you find a key\n written on it is, Attic")
        attic_key = True
        choose()

def look_attic():
    global cell_key
    if cell_key:
        look_nothing()
    else:
        print("\nLifting the rug up you find yet another key\nthis time written on the key is, Cell")
        cell_key = True
        choose()

def look_outside():
    global rock
    if rock:
        look_nothing()
    elif entry_open:
        look_nothing()
    else:
        print("\nOn the ground you find a rock, maybe you can use this")
        rock = True
        choose()
        
#Dictionary of all rooms and connections
Castle = {
    "outside": {
        "enter basement": basement,
        "enter castle": entry,
        "look around": look_outside,
        "quit": lambda: sys.exit("goodbye")
        },
    "entry": {
        "go outside": outside,
        "go to center room": center,
        "examine vase": lambda: examine_empty("vase"),
        "look around": look_nothing,
        "quit": lambda: sys.exit("goodbye")
        },
    "center room": {
        "go to entry": entry,
        "go to east hall": east_hall,
        "go to west hall": west_hall,
        "go to balcony": balcony,
        "look around": look_nothing,
        "quit": lambda: sys.exit("goodbye")
        },
    "west hall": {
        "enter basement": basement,
        "go to attic": attic,
        "go to center room": center,
        "look around": look_nothing,
        "quit": lambda: sys.exit("goodbye")
        },
    "east hall": {
        "enter master bedroom": master_bed,
        "enter guest bedroom": guest_bed,
        "go to center room": center,
        "look around": look_nothing,
        "quit": lambda: sys.exit("goodbye")
        },
    "basement": {
        "go to west hall": west_hall,
        "go outside": outside,
        "enter basement hall": basement_hall,
        "look around": look_nothing,
        "quit": lambda: sys.exit("goodbye")
        },
    "attic": {
        "exit attic": west_hall,
        "lift rug": look_attic,
        "quit": lambda: sys.exit("goodbye")
        },
    "balcony": {
        "go to center room": center,
        "look around": look_nothing,
        "quit": lambda: sys.exit("goodbye")
        },
    "basement hall": {
        "enter cell": cell,
        "enter study": study,
        "leave hall": basement,
        "look around": look_nothing,
        "quit": lambda: sys.exit("goodbye")
        },
    "study": {
        "check desk": examine_study,
        "leave study": basement_hall,
        "quit": lambda: sys.exit("goodbye")
        },
    "guest bedroom":{
        "leave bedroom": east_hall,
        "look around": look_nothing,
        "quit": lambda: sys.exit("goodbye")
        },
    "master bedroom": {
        "leave bedroom": east_hall,
        "look around": look_master,
        "quit": lambda: sys.exit("goodbye")
        },
    
    }

#print(Castle)
start()
outside()

