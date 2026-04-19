import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys, random, time

#Config
root = tk.Tk()
root.title("Battle Game")
frm = ttk.Frame(root, padding=2)
frm.grid()
fight_options = ttk.Frame(frm, padding=2)
act_options = ttk.Frame(frm, padding=2)
items_options = ttk.Frame(frm, padding=2)
flee_options = ttk.Frame(frm, padding=2)
message_box_frame = ttk.Frame(frm, padding=2)
message_box_frame.grid(column=1, row=3)

#Style and colors
style = ttk.Style()
style.theme_use("alt")

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

#Define variables
current_enemy = None
flee_chance = 5
player_health = 20
enemy_health = 20
player_damage = 5
fight_open = False
act_open = False
flee_open = False
items_open = False
enemys = ["Troll", "Goblin", "Vampire", "Ghost", "Slime", "Cyclops", "Ogre", "Dragon"]

#Define functions

def get_enemy():
    global enemy_health, current_enemy    
    current_enemy = random.choice(enemys)
    if current_enemy == "Troll":
      enemy_health = 10
    elif current_enemy == "Goblin":
      enemy_health = 15
    elif current_enemy == "Vampire":
      enemy_health = 20
    elif current_enemy == "Ghost":
        enemy_health = 10
    elif current_enemy == "Slime":
        enemy_health = 5
    elif current_enemy == "Cyclops":
        enemy_health = 30
    elif current_enemy == "Ogre":
        enemy_health == 25
    elif current_enemy == "Dragon":
        enemy_health = 40

def game_tick():
    upd_health_display()
    #print("game tick")
    root.after(1000, game_tick)

def message(text, time):
    root.after(time, lambda: message_box.config(text=text))

def enemy_attack():
    global player_health
    if random.randint(0, 10) >= 7:
        message_box.config(text=f"The {current_enemy} hit you!")
        message("You lost 2 health", 1000)
        player_health = player_health - 2
    else:
        message_box.config(text=f"The {current_enemy} tried to hit you")
        message("But failed", 1000)

def player_attack(num1, num2, num3):
    global enemy_health, player_damage
    if random.randint(num1, num2) >= num3:
        message_box.config(text=f"You hit the {current_enemy}!")
        enemy_health = enemy_health - player_damage
        message(f"The enemy lost {player_damage} HP", 1000)
    else:
        message_box.config(text=f"You tried to hit the {current_enemy}")
        message("But failed", 1000)
        root.after(3000, enemy_attack)

def upd_health_display():
    global player_health
    if player_health <= 0:
        message_box.config(text="You lost!!")
        root.after(3000, root.destroy)
    elif enemy_health <= 0:
        message_box.config(text="You Win!!")
        root.after(3000, root.destroy)
    else:
        pl_hp_display.config(text=f"Player HP: {player_health}")
        en_hp_display.config(text=f"{current_enemy} HP: {enemy_health}")

def close_options():
    global fight_open, act_open, items_open, flee_open
    fight_open = False
    act_open = False
    items_open = False
    flee_open = False
    act_options.grid_remove()
    fight_options.grid_remove()
    items_options.grid_remove()
    flee_options.grid_remove()
def fight():
    global fight_open, act_open, items_open, flee_open
    if fight_open == True:
        close_options()
    else:
        close_options()
        fight_open = True
        fight_options.grid(column=1, row=2)
        
def fight_fists_func():
    global player_health
    close_options()
    player_attack(0, 3, 2)
    
def fight_sword_func():
    close_options()
    player_attack(0, 4, 2)
def act():
    global act_open, fight_open, items_open, flee_open
    if act_open == True:
        close_options()
    else:
        close_options()
        act_open = True
        act_options.grid(column=2, row=2)
        
        
def act_backflip_func():
    global player_health
    close_options()
    if random.randint(0, 10) >= 5:
        message_box.config(text="You did a sick backflip")
        message(f"The {current_enemy} decided to leave you alone", 2000)
        root.after(4000, root.destroy)
    else:
        message_box.config(text="You tried to do a backflip but failed")
        message("You take 5pts of damage", 1000)
        player_health = player_health - 5
    close_options

def act_compliment_func():
    global player_health, enemy_health
    close_options()
    message_box.config(text=f"You compliment the {current_enemy}")
    if random.randint(0, 10) >= 5:
        message("It loved your compliment!", 1000)
        message(f"The {current_enemy} lost {player_damage} HP!", 3000)
        enemy_health = enemy_health - player_damage
    else:
        message("Your compliment didn't land", 1000)

def act_play_dead_func():
    global player_health, enemy_health
    close_options()
    if random.randint(0, 10) >= 7:
        message_box.config(text="You play dead")
        message("You were able to sneak up on the enemy", 1000)
        message(f"The enemy lost {player_damage} HP", 4000)
        enemy_health = enemy_health - player_damage
    else:
        message_box.config(text="You tried to play dead")
        message("But failed", 1000)
        message("You lost 2 HP", 3000)
        player_health = player_health - 2

def items():
    global act_open, fight_open, items_open, flee_open
    if items_open == True:
        close_options()
    else:
        close_options()
        items_open = True
        items_options.grid(column=3, row=2)

def items_heal_pot_func():
    global player_health
    close_options()
    message_box.config(text="You used a healing potion")
    message("+5 HP", 1000)
    player_health = player_health + 2
    items_heal_pot.config(state="disabled")
    close_options()

def items_Steroids_func():
    global player_damage
    close_options()
    message_box.config(text="You used the Steroids")
    message("+2 damage", 1000)
    player_damage = player_damage + 2
    items_steroids.config(state="disabled") 
    

def items_speed_pot_func():
    global flee_chance
    close_options()
    message_box.config(text="You used the Speed potion")
    message("+2 Flee chance", 2000)
    flee_chance=3
    items_speed_pot.config(state="disabled")
    close_options()

def flee():
    global act_open, fight_open, items_open, flee_open
    if flee_open == True:
        close_options()
    else:
        close_options()
        flee_open = True
        flee_options.grid(column=4, row=2)

def flee_yes_func():
    if random.randint(0, 10) >= flee_chance:
        close_options()
        message_box.config(text="You succesfully flee (coward)")
        root.after(2000, root.destroy)
    else:
        close_options()
        message_box.config(text="You failed to flee")
        message("You can no longer flee", 1000)
        flee_button.config(state="disabled")
        flee_button.config(style="LightPurple.TButton")
        
#Gui (Buttons, Labels, etc)
pl_hp_display = ttk.Label(frm, text=f"Player HP: {player_health}")
en_hp_display = ttk.Label(frm, text=f"{current_enemy} HP: {enemy_health}")
message_box = ttk.Label(frm, text="Actions show up here", font=("TkDefaultFont", 15))
act_button = ttk.Button(frm, text="Act", command=act, style="Blue.TButton")
act_backflip = ttk.Button(act_options, text="Backflip", command=act_backflip_func, style="Sky.TButton")
act_compliment = ttk.Button(act_options, text="Compliment", command=act_compliment_func, style="Sky.TButton")
act_play_dead = ttk.Button(act_options, text="Play Dead", command=act_play_dead_func, style="Sky.TButton")
fight_button = ttk.Button(frm, text="Fight", command=fight, style="Red.TButton")
fight_fists = ttk.Button(fight_options, text="Fists", command=fight_fists_func, style="Pink.TButton")
fight_sword = ttk.Button(fight_options, text="Sword", command=fight_sword_func, style="Pink.TButton")
items_button = ttk.Button(frm, text="Items", command=items, style="Green.TButton")
items_heal_pot = ttk.Button(items_options, text="Healing Potion", command=items_heal_pot_func, style="LightGreen.TButton")
items_steroids = ttk.Button(items_options, text="Steroids", command=items_Steroids_func, style="LightGreen.TButton")
items_speed_pot = ttk.Button(items_options, text="Speed Potion", command=items_speed_pot_func, style="LightGreen.TButton")
flee_button = ttk.Button(frm, text="Flee", command=flee, style="Purple.TButton")
flee_question = ttk.Label(flee_options, text="Are you sure?")
flee_yes = ttk.Button(flee_options, text="Yes", command=flee_yes_func, style="LightPurple.TButton")
flee_no = ttk.Button(flee_options, text="No", command=close_options, style="LightPurple.TButton")
pl_hp_display.grid(column=1, row=0)
en_hp_display.grid(column=2, row=0, padx=3)
message_box.grid(column=1, row=5, columnspan=5)
fight_button.grid(column=1, row=1, padx=3)
fight_fists.grid(column=1, row=2)
fight_sword.grid(column=1, row=3)
act_button.grid(column=2, row=1, padx=3)
act_backflip.grid(column=2, row=2)
act_compliment.grid(column=2, row=3)
act_play_dead.grid(column=2, row=4)
items_button.grid(column=3, row=1, padx=3)
items_heal_pot.grid(column=3, row=2)
items_steroids.grid(column=3, row=3)
items_speed_pot.grid(column=3, row=4)
flee_button.grid(column=4, row=1, padx=3)
flee_question.grid(column=4, row=2)
flee_yes.grid(column=4, row=3)
flee_no.grid(column=4, row=4)

#Run the program
get_enemy()
game_tick()
root.mainloop()
