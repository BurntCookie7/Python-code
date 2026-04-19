import random, sys

#Variables
current_room = "outside"

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
    print("\nAs you enter the basement you are hit with a horrible stench\nits cold and dark")
    print("There is a path outside to your left,\nto your right there is a spiral staircase up to the east hall of the castle,\nin front of you there is a hallway")
    choose()

def entry():
    global current_room
    if current_room == "outside":
        current_room = "outside"
        print("\nThe door is boarded shut")
        outside()
    else:
        current_room = "entry"
        print("\nYou step into the entry of the castle\ntheres a vase in the corner\nthere are brick walls to your left and right\nit's cold")
        print("Ahead of you leads to the center room of the castle,\nbehind you is the door exiting the castle")
        choose()

def east_hall():
    global current_room
    current_room = "east hall"
    print("\nYou enter the east hall\nlike the west hall it is dark")
    print("You are facing towards a spiral staircase to the basement,\nabove you is the entrance to the attic,\nbehind you the east hall leads to the center room of the castle")
    choose()

def west_hall():
    global current_room
    current_room = "west hall"
    print("\nYou enter the west hall\nlike the east hall it is dark")
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
    current_room = "east hall"
    print("\nIt's locked")
    print("you need to find a key")
    choose()

def guest_bed():
    global current_room
    current_room = "guest bedroom"
    print("\nYou enter the guest bedroom")
    print("There's nothing notable in this room")
    choose()

def attic():
    global current_room
    current_room = "east hall"
    print("\nIt's locked")
    print("you need to find a key")
    choose()

#def examine_empty(item):
    print(f"\nYou look in the {item}\nthere is nothing")
    choose()

def basement_hall():
    global current_room
    current_room = "basement hall"
    print("\nYou walk through the brick walls of the basement into a slim hallway")
    print("To your left there is a door leading to the cell,\nto your right lies the vampires study")
    choose()

def cell():
    print("\nIt's locked")
    print("you need to find a key")
    choose()

def study():
    global current_room
    current_room = "study"
    print("\nYou enter the study,\nits filled with books, there are papers scattered around the desk and floor")
    choose()
    
    
#Dictionary of all rooms and connections
Castle = {
    "outside": {
        "enter basement": basement,
        "enter castle": entry,
        "quit": sys.exit
        },
    "entry": {
        "go outside": outside,
        "go to center room": center,
        #"examine vase": lambda: examine_empty(vase),
        "quit": sys.exit
        },
    "center room": {
        "go to entry": entry,
        "go to east hall": east_hall,
        "go to west hall": west_hall,
        "go to balcony": balcony,
        "quit": sys.exit
        },
    "east hall": {
        "enter basement": basement,
        "go to attic": attic,
        "go to center room": center,
        "quit": sys.exit
        },
    "west hall": {
        "enter master bedroom": master_bed,
        "enter guest bedroom": guest_bed,
        "go to center room": center,
        "quit": sys.exit
        },
    "basement": {
        "go to east hall": east_hall,
        "go outside": outside,
        "enter basement hall": basement_hall,
        "quit": sys.exit
        },
    "attic": {
        "exit attic": east_hall,
        "quit": sys.exit
        },
    "balcony": {
        "go to center room": center,
        "quit": sys.exit
        },
    "basement hall": {
        "enter cell": cell,
        "enter study": study,
        "leave hall": basement,
        "quit": sys.exit
        },
    
    }

#print(Castle)
start()
outside()

