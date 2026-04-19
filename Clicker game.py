import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import math
import threading
import sys
#clps = clicks per second


def game_tick():
    clps()
    root.after(1000, game_tick)

#the function that runs every second for the Clicks per Second upgrade
def clps():
    global upgrade_price, points_counter, score, click_amount, score_display, clps_amount
    score = score + clps_amount
    score_display = int(score)
    update_window()
    print(f"{score_display} points")

#creates a new thread
thread_2 = threading.Thread(target=clps)
#the function that runs when you buy the clicks per second upgrade
def clps_upgrade():
    global clps_amount, score, click_amount, clps_price
    if score >= clps_price:
        score = score - clps_price
        print("+1 Clicks per Second")
        clps_amount = clps_amount + 1
        clps_price = clps_price * 1.3
        clps_price = int(clps_price)
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
    global upgrade_price, score
    upgrade_price_number = int(upgrade_price)
    score_display = int(score)
    score_counter.config(text=f"{score_display} Clicks")
    upgrade_price_display.config(text=f"Cost: {upgrade_price_number}")
    if score >= 100000:
        win_button.grid(column=2, row=3)

def win():
    sys.exit("You Win!!")
    win_button.config(column=0, row=0)


def debug():
    global score
    score = int(input("Enter a score"))
    update_window()

#Configuration
score = 0
score_display = int(score)
upgrade_price = 2
upgrade_price_number = int(upgrade_price)
click_amount = 1
clps_amount = 0
clps_price = 5
root = Tk()
frm = ttk.Frame(root, padding=3)
frm.grid()
root.title("Clicker Game")

#Gui (Buttons, Labels, etc)
button = ttk.Button(frm, text="Click Me", command=on_button_clicked)
upgrade_button = ttk.Button(frm, text="Clicks Upgrade", command=upgrade_clicked)
shop_text = ttk.Label(frm, text="Store", font=("TkDefaultFont", 15))
clps_button = ttk.Button(frm, text="CLPS Upgrade", command=clps_upgrade)
win_button = ttk.Button(frm, text="Win (optional)", command=win)
upgrade_price_display = ttk.Label(frm, text="Cost: 2")
clps_price_display = ttk.Label(frm, text="Cost: 5")
score_counter = ttk.Label(frm, text=f"{score_display} Clicks")
debug = ttk.Button(frm, text="Debug", command=debug)
button.grid(column=0, row=6, ipadx=3, ipady=4)
upgrade_button.grid(column=0, row=2)
shop_text.grid(column=0, row=1)
score_counter.grid(column=0, row=7)
upgrade_price_display.grid(column=0, row=3)
clps_button.grid(column=0, row=4)
clps_price_display.grid(column=0, row=5)
#Run the program
debug_mode = False
if debug_mode:
    debug.grid(column=0, row=3)
game_tick()
root.mainloop()



