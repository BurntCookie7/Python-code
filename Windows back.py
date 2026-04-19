import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import math
def on_button_clicked():
    global upgrade_price
    global points_counter
    global score
    global click_amount
    global score_display
    upgrade_price = int(upgrade_price)
    score = score + click_amount
    score_display = int(score)
    update_score()
    print(f"{score_display} points")
    time.sleep(0.1)
def upgrade_clicked():
    global score
    global click_amount
    global upgrade_price
    global upgrade_price_number
    global score_display
    if score >= upgrade_price:
        print("+1 points per click!")
        upgrade_price = upgrade_price * 1.3
        upgrade_price_display = int(upgrade_price)
        click_amount = click_amount + 1
        score = score - upgrade_price
        update_score()
        print(f"{score_display} points")
        
        time.sleep(0.1)
    else:
        print("Not enough Clicks")
def update_score():
    global upgrade_price
    upgrade_price_number = int(upgrade_price)
    score_display = int(score)
    score_counter.config(text=f"{score_display} Clicks")
    upgrade_price_display.config(text=f"Cost: {upgrade_price_number}")
score = 0
score_display = int(score)
upgrade_price = 1.5
upgrade_price_number = int(upgrade_price)
click_amount = 1
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
root.title("Clicker Game")
ttk.Button(frm, text="Click Me", command=on_button_clicked).grid(column=2, row=1)
ttk.Button(frm, text="Upgrade", command=upgrade_clicked).grid(column=0, row=1)
upgrade_price_display=ttk.Label(frm, text="Cost: 2")
upgrade_price_display.grid(column=0, row=2)
score_counter=ttk.Label(frm, text=f"{score_display} Clicks")
score_counter.grid(column=2, row=2)
root.mainloop()
