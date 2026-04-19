import tkinter as tk
from tkinter import *
from tkinter import ttk
import time, math, sys, json
#clps = clicks per second


def game_tick():
    clps()
    autosave()
    root.after(1000, game_tick)

#the function that runs every second for the Clicks per Second upgrade
def clps():
    global upgrade_price, points_counter, score, click_amount, score_display, clps_amount
    score = score + clps_amount
    score_display = int(score)
    update_window()
    print(f"{score_display} points")


#the function that runs when you buy the clicks per second upgrade
def clps_upgrade():
    global clps_amount, score, click_amount, clps_price, clps_price_amount
    if score >= clps_price_amount:
        score = score - clps_price_amount
        print("+1 Clicks per Second")
        clps_amount = clps_amount + 1
        clps_price = clps_price * 1.25
        clps_price_amount = int(clps_price)
        update_window()
    else:
        print("Not enough Clicks")

#adds points when the "Click Me" button is clicked
def on_button_clicked():
    global upgrade_price, points_counter, score, click_amount, score_display
    upgrade_price = int(upgrade_price)
    score = score + click_amount
    score_display = int(score)
    update_window()
    print(f"{score_display} points")

#runs when the basic upgrade is purchased
def upgrade_clicked():
    global score, click_amount, upgrade_price, upgrade_price_display, score_display, upgrade_price_number
    if score >= upgrade_price_number:
        score = score - upgrade_price_number
        upgrade_price = upgrade_price * 1.3
        upgrade_price_number = int(upgrade_price)
        click_amount = click_amount + 1
        update_window()
        print(f"{score_display} points")
        #print(upgrade_price)
        print("+1 points per click!")
    else:
        print("Not enough Clicks")
        
#refreshes/updates the game window making sure everything is as it should be
def update_window():
    global upgrade_price, score, clps_price, clps_price_amount, upgrade_price_number
    upgrade_price_number = int(upgrade_price)
    score_display = int(score)
    clps_price_amount = int(clps_price)
    score_counter.config(text=f"{score_display} Clicks")
    upgrade_price_display.config(text=f"Cost: {upgrade_price_number}")
    clps_price_display.config(text=f"Cost: {clps_price_amount}")
    status.config(text=f"Clicks={click_amount}\nClicks per Second={clps_amount}")
    

def win():
    sys.exit("You Win!!")
    win_button.config(column=0, row=0)


def debug():
    global score
    score = int(input("Enter a score\n"))
    update_window()

def save():
    global score, click_amount, upgrade_price, clps_amount, clps_price
    data = {"score": score, "click_amount": click_amount, "upgrade_price": upgrade_price, "clps_amount": clps_amount, "clps_price": clps_price}
    with open("save_data.json", "w") as f:
        json.dump(data, f)
    print("Data saved")

def autosave():
    global score, click_amount, upgrade_price, clps_amount, clps_price
    data = {"score": score, "click_amount": click_amount, "upgrade_price": upgrade_price, "clps_amount": clps_amount, "clps_price": clps_price}
    with open("save_data.json", "w") as f:
        json.dump(data, f)

def load():
    global score, click_amount, upgrade_price, clps_amount, clps_price
    try:
        with open("save_data.json", "r") as f:
            data = json.load(f)
            score = data["score"]
            click_amount = data["click_amount"]
            upgrade_price = data["upgrade_price"]
            clps_amount = data["clps_amount"]
            clps_price = data["clps_price"]
            
            print("Loaded data")
    except (FileNotFoundError, KeyError):
        print("Save file not found or corrupted.")

def clear_save_func():
    global score, score_display, upgrade_price, upgrade_price_number, click_amount, clps_amount, clps_price, clps_price_amount
    if input("Are you sure? y/n\n") == "y":
        score = 0
        score_display = int(score)
        upgrade_price = 2
        upgrade_price_number = int(upgrade_price)
        click_amount = 1
        clps_amount = 0
        clps_price = 5
        clps_price_amount = int(clps_price)
        update_window()
        save()
        

#Configuration
score = 0
score_display = int(score)
upgrade_price = 2
upgrade_price_number = int(upgrade_price)
click_amount = 1
clps_amount = 0
clps_price = 5
clps_price_amount = int(clps_price)
root = Tk()
frm = ttk.Frame(root)
frm.grid(sticky="nwes")
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)
root.title("Clicker Game")

#Style and colors
style = ttk.Style(frm)
style.theme_use("default")

style.configure("Red.TButton", background="red", foreground="white")
style.configure("Blue.TButton", background="blue", foreground="white")
style.configure("Green.TButton", background="green", foreground="white")
style.configure("Sky.TButton", background="#87e7ff", foreground="white")
style.configure("Pink.TButton", background="#ff87b7", foreground="white")
style.configure("Purple.TButton", background="purple", foreground="white")
style.configure("LightGreen.TButton", background="#7bd66f", foreground="white")
style.configure("LightPurple.TButton", background="#9c6fd6", foreground="white")
style.map("Pink.TButton", background=[("active", "red")], foreground=[("active", "white")])
style.map("Sky.TButton", background=[("active", "blue")], foreground=[("active", "white")])
style.map("Red.TButton", background=[("active", "#f25f55")], foreground=[("active", "white")])
style.map("Blue.TButton", background=[("active", "#5565f2")], foreground=[("active", "white")])
style.map("Green.TButton", background=[("active", "#6ca854")], foreground=[("active", "white")])
style.map("Purple.TButton", background=[("active", "#8f55f2")], foreground=[("active", "white")])
style.map("LightGreen.TButton", background=[("active", "green")], foreground=[("active", "white")])
style.map("LightPurple.TButton", background=[("active", "purple")], foreground=[("active", "white")])





#Gui (Buttons, Labels, etc)
button = ttk.Button(frm, text="Click Me", command=on_button_clicked, style="Blue.TButton")
upgrade_button = ttk.Button(frm, text="Clicks Upgrade", command=upgrade_clicked)
shop_text = ttk.Label(frm, text="Store", font=("TkDefaultFont", 15))
clps_button = ttk.Button(frm, text="CLPS Upgrade", command=clps_upgrade)
upgrade_price_display = ttk.Label(frm, text="Cost: 2")
clps_price_display = ttk.Label(frm, text="Cost: 5")
score_counter = ttk.Label(frm, text=f"{score_display} Clicks")
save_button = ttk.Button(frm, text="Save Data", command=save)
load_button = ttk.Button(frm, text="Load Data", command=load)
clear_save = ttk.Button(frm, text="Clear save", command=clear_save_func)
status = ttk.Label(frm, text=f"Clicks={click_amount}\nClicks per Second={clps_amount}")
gap1 = ttk.Label(frm, text="------------------------")
gap2 = ttk.Label(frm, text="------------------------")
button.grid(column=0, row=8, ipady=10, ipadx=7)
upgrade_button.grid(column=0, row=2)
shop_text.grid(column=0, row=1)
score_counter.grid(column=0, row=9)
upgrade_price_display.grid(column=0, row=3)
clps_button.grid(column=0, row=4)
clps_price_display.grid(column=0, row=5)
save_button.grid(column=0, row=11)
#load_button.grid(column=0, row=10)
clear_save.grid(column=0, row=12)
status.grid(column=0, row=7)
gap1.grid(column=0, row=10)
gap2.grid(column=0, row=6)

#Run the program
debug_mode = False
if debug_mode:
    debug = ttk.Button(frm, text="Debug", command=debug, style="Red.TButton")
    debug.grid(column=1, row=1)
load()
game_tick()
root.mainloop()



