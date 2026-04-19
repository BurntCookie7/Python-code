import random, sys

#Variables
current_room = "outside"
master_key = False
attic_key = False
cell_key = False
rock = False
entry_open = False

#Functions
def start():
    input("To choose a action just type its number\nQuitting exits the game\nProgress is not saved\npress ENTER to continue")
    print("\nYour sister has been taken by a vampire")

def outside():
    global current_room
    current_room = "outside"
    print("\nYou are outside in front of a castle")
    print("Ahead of you is the entrance to the castle,\naround the castle there is a grate leading to the basement\nthe grate can be pulled away")
    print("\nYou can do the following:")
    print("1. Enter the basement")
    if entry_open:
        print("2. Enter castle")
    else:
        print("2. Check the door")
    print("3. Look around")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        basement()
    elif choice == "2":
        entry()
    elif choice == "3":
        look_outside()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        outside()

def center():
    global current_room
    current_room = "center room"
    print("\nYou walk into the center of the castle")
    print("Behind you is the entryway of the castle,\nahead there are stairs leading to the balcony\nto your left is the east hall\n to your right is the west hall")
    print("\nYou can do the following:")
    print("1. Enter the East hall")
    print("2. Enter the West hall")
    print("3. Walk to the Entry hall")
    print("4. Walk up to the Balcony")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        east_hall()
    elif choice == "2":
        west_hall()
    elif choice == "3":
        entry()
    elif choice == "4":
        balcony()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        center()

def basement():
    global current_room
    current_room = "basement"
    print("\nAs you enter the basement you are hit with a horrible stench\nits cold and dark")
    print("There is a path outside to your left,\nto your right there is a spiral staircase up to the east hall of the castle,\nin front of you there is a hallway")
    print("\nYou can do the following:")
    print("1. Go outside")
    print("2. Go upstairs")
    print("3. Enter hallway")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        outside()
    elif choice == "2":
        east_hall()
    elif choice == "3":
        basement_hall()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        basement()
        
def entry():
    global current_room, rock, entry_open
    if current_room == "outside":
        if rock == True:
            print("\nWith the rock you manage to break the boards holding the door shut")
            rock = False
            entry_open = True
            outside()
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
        print("\nYou can do the following:")
        print("1. Go back to center room")
        print("2. check door")
        print("3. Check vase")
        print("Q. Quit")
        choice = input()
    if choice == "1":
        center()
    elif choice == "2":
        print("The door is boarded shut")
        entry()
    elif choice == "3":
        item_look_nothing("vase")
        entry()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        entry()
        
def east_hall():
    global current_room
    current_room = "east hall"
    print("\nYou enter the east hall\nlike the west hall it is dark")
    print("You are facing towards a spiral staircase to the basement,\nabove you is the entrance to the attic,\nbehind you the east hall leads to the center room of the castle")
    print("\nYou can do the following:")
    print("1. Check attic")
    print("2. Go downstairs")
    print("3. Go to center room")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        attic()
    elif choice == "2":
        basement()
    elif choice == "3":
        center()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        east_hall()

def west_hall():
    global current_room
    current_room = "west hall"
    print("\nYou enter the west hall\nlike the east hall it is dark")
    print("You are facing towards the guest bedroom,\nto your left is the master bedroom,\nbehind you is the center room of the castle")
    print("\nYou can do the following:")
    print("1. Enter Master bedroom")
    print("2. Enter Guest bedroom")
    print("3. Go to center room")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        master_bed()
    elif choice == "2":
        guest_bed()
    elif choice == "3":
        center()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        west_hall()

def balcony():
    global current_room
    current_room = "balcony"
    print("\nClimbing up the stairs in the center room you arrive on the balcony,\nthere is a light breeze")
    print("Behind you a set of stairs leads to the center room of the castle")
    print("\nYou can do the following:")
    print("1. Go to center room")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        center()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        balcony()

def master_bed():
    global current_room
    if master_key:
        print("\nYou can do the following")
        print("1. Exit master bedroom")
        print("2. Look around")
        print("Q. Quit")
        choice = input()
        if choice == "1":
            west_hall()
        elif choice == "2":
            look_master()
        elif choice == "Q" or choice == "q":
            sys.exit("Goodbye!!")
    else:
        current_room = "east hall"
        print("\nIt's locked")
        print("you need to find a key")
        west_hall()

def guest_bed():
    global current_room
    current_room = "guest bedroom"
    print("\nYou enter the guest bedroom")
    print("There's nothing notable in this room")
    print("\nYou can do the following:")
    print("1. Enter West hall")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        west_hall()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        guest_bed()

def attic():
    global current_room
    if attic_key == True:
        if cell_key == False:
            print("\nThe attic is dusty\nthere is a rug on the floor with a strange bump in the middle")
        else:
            print("\nThe attic is dusty\nthere is a rug on the floor")
        print("\nYou can do the following:")
        print("1. examine rug")
        print("2. Leave attic")
        print("Q. Quit")
        choice = input()
        if choice == "1":
            look_attic()
        elif choice == "2":
            east_hall()
        elif choice == "Q" or choice == "q":
            sys.exit("Goodbye!!")
        else:
                print(f"{choice} is not a valid option")
    else:
        current_room = "east hall"
        print("\nIt's locked")
        print("you need to find a key")
        east_hall()
        


def item_look_nothing(item):
    print(f"\nYou look in the {item}\nthere is nothing")


def basement_hall():
    global current_room
    current_room = "basement hall"
    print("\nYou walk through the brick walls of the basement into a slim hallway")
    print("To your left there is a door leading to the cell,\nto your right lies the vampires study")
    print("\nYou can do the following:")
    print("1. Leave hall")
    print("2. Check cell door")
    print("3. Enter study")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        basement()
    elif choice == "2":
        cell()
    elif choice == "3":
        study()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        basement_hall()

def cell():
    if cell_key == True:
        print("\nYou are in the cell, inside you finally find your sister\nshe has been saved from the vapire that took her")
        sys.exit("You win")
    else:
        print("\nIt's locked")
        print("you need to find a key")
        basement_hall()

def study():
    global current_room
    current_room = "study"
    print("\nYou enter the study,\nits filled with books, there are papers scattered around the desk and floor")
    print("\nYou can do the following:")
    print("1. Leave study")
    print("2. Examine desk")
    print("Q. Quit")
    choice = input()
    if choice == "1":
        basement_hall()
    elif choice == "2":
        look_study()
    elif choice == "Q" or choice == "q":
        sys.exit("Goodbye!!")
    else:
        print(f"{choice} is not a valid option")
        study()

def look_study():
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
    

def look_master():
    global attic_key
    if attic_key:
        look_nothing()
        master_bed()
    else:
        print("\nSitting on a nightstand you find a key\n written on it is, Attic")
        attic_key = True
    master_bed()

def look_attic():
    global cell_key
    if cell_key:
        look_nothing()
        attic()
    else:
        print("\nLifting the rug up you find yet another key\nthis time written on the key is, Cell")
        cell_key = True
    attic()

def look_outside():
    global rock
    if rock:
        look_nothing()
        outside()
    elif entry_open:
        look_nothing()
        outside()
    else:
        print("\nOn the ground you find a rock, maybe you can use this")
        rock = True
    outside()



#print(Castle)
start()
outside()

