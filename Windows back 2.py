import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import math
#clps = clicks per second

#the function that runs every second for the Clicks per Second upgrade
def clps():
    global upgrade_price
    global points_counter
    global score
    global click_amount
    global score_display
    global clps_amount
    score = score + clps_amount
    score_display = int(score)
    update_window()
    print(f"{score_display} points")
    time.sleep(0.1)

#the function that runs when you buy the clicks per second upgrade
def clps_upgrade():
    clps_amount + 1

#adds points when the "Click Me" button is clicked
def on_button_clicked():
    global upgrade_price
    global points_counter
    global score
    global click_amount
    global score_display
    upgrade_price = int(upgrade_price)
    score = score + click_amount
    score_display = int(score)
    update_window()
    print(f"{score_display} points")
    time.sleep(0.1)

#runs when the basic upgrade is purchased
def upgrade_clicked():
    global score
    global click_amount
    global upgrade_price
    global upgrade_price_number
    global score_display
    if score >= upgrade_price_number:
        score = score - upgrade_price_number
        upgrade_price = upgrade_price * 1.3
        upgrade_price_number = int(upgrade_price)
        click_amount = click_amount + 1
        update_window()
        print(f"{score_display} points")
        #print(upgrade_price)
        print("+1 points per click!")
        time.sleep(0.1)
    else:
        print("Not enough Clicks")
#refreshes/updates the game window making sure everything is as it should be
def update_window():
    global upgrade_price
    upgrade_price_number = int(upgrade_price)
    score_display = int(score)
    score_counter.config(text=f"{score_display} Clicks")
    upgrade_price_display.config(text=f"Cost: {upgrade_price_number}")

#configuration
score = 0
score_display = int(score)
upgrade_price = 2
upgrade_price_number = int(upgrade_price)
click_amount = 1
clps_amount = 0
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
root.title("Clicker Game")


#Gui (Buttons, Labels, etc)
ttk.Button(frm, text="Click Me", command=on_button_clicked).grid(column=2, row=1)
ttk.Button(frm, text="Clicks Upgrade", command=upgrade_clicked).grid(column=0, row=1)
ttk.Button(frm, text="CLPS Upgrade", command=clps_upgrade).grid(column=0, row=3)
upgrade_price_display=ttk.Label(frm, text="Cost: 2")
upgrade_price_display.grid(column=0, row=2)
score_counter=ttk.Label(frm, text=f"{score_display} Clicks")
score_counter.grid(column=2, row=2)

#run the program
root.mainloop()


