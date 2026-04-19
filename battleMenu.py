import random
import time
import sys
won = False
def enemy_attack():
    global player_health
    enemy_hits = random.choice(does_succeed)
    print("The enemy tries to attack you!")
    time.sleep(1)
    if enemy_hits == True:
        print("The enemy attack landed!")
        time.sleep(1)
        player_health = int(player_health) - 2
        print(f"You are at {player_health}hp")
        time.sleep(1)
    else:
        print("The enemy attack missed!")
        time.sleep(1)
def win():
    print("You Win!!!")
    time.sleep(.5)
    print("Everybody cheers for the monster was slain!")
    time.sleep(2)
    for i in range(5):
        print("Hooray!!")
        time.sleep(.2)
        print("yipee!")
    sys.exit("The End")
def battle():
    global current_health
    global enemy_health
    global won
    print(f"you are fighting a {current_enemy}")
    print(f"the enemy has {enemy_health}hp")
    print("pick an option")
    battle_choice = input("1<FIGHT>  2<ACT>  3<FLEE>")
    if battle_choice == "1":
        hit_chance = random.randint(1,10)
        if hit_chance >= 4:
            print(f"Your attack hits, you deal 2pts of dammage to the {current_enemy}")
            enemy_health = int(enemy_health) - 2
            print(f"The enemy is at {enemy_health}hp")
            time.sleep(1)
            if enemy_health <= 0:
                won = True
        else:
              print("you did not hit the enemy")
              time.sleep(1)
    elif battle_choice == "2":
            print("pick an action")
            action_choice = input("1<BACKFLIP> 2<TRICK> 3<LOOK COOL>")
            if action_choice == "1":
                print("you do an awesome backflip")
                time.sleep(1)
                print("it does nothing...")
                time.sleep(1)
            elif action_choice == "2":
                trick_success = random.randint(1, 10)
                if trick_success >= 5:
                    print(f"you showed the {current_enemy} a trick")
                    time.sleep(1)
                    print(f"the {current_enemy} was impressed, it decided to leave you alone.")
                    time.sleep(0.5)
                    win()
                else:
                    print("The enemy was not impressed")
                    time.sleep(0.5)
            elif action_choice == "3":
                monster_impressed = random.choice(does_succeed)
                if monster_impressed == True:
                    print("The monster is impressed")
                    time.sleep(1)
                    win()
                else:
                    print("you fail to impress the monster")
    elif battle_choice == "3":
        flee_chance = random.choice(does_succeed)
        if flee_chance == True:
            print("you fleed the battle")
            time.sleep(1)
            sys.exit("coward")
        else:
            print("you failed to flee")
            time.sleep(1)
    if player_health <= 0:
        sys.exit("You Died")
    else:
        if won == True:
            win()
        else:
            print(f"you have {player_health}hp")
            enemy_attack()
            battle()
does_succeed = [True, False]
enemys = ["troll", "goblin", "vampire", "ghost", "slime", "cyclops", "ogre", "Dragon"]
def get_enemy():
    global enemy_health    
    global current_enemy
    current_enemy = random.choice(enemys)
    if current_enemy == "troll":
      enemy_health = 10
    elif current_enemy == "goblin":
      enemy_health = 15
    elif current_enemy == "vampire":
      enemy_health = 20
    elif current_enemy == "ghost":
        enemy_health = 10
    elif current_enemy == "slime":
        enemy_health = 5
    elif current_enemy == "cyclops":
        enemy_health = 30
    elif current_enemy == "ogre":
        enemy_health == 25
    elif current_enemy == "Dragon":
        enemy_health = 40
#print("#DISCLAMER, TH#")
enemy_health = 0
current_health = enemy_health
current_enemy = None
enemy_hits = None
player_health = 10
get_enemy()
print("It's a normal day in the kingdom not a worry in the world...")
time.sleep(0.5)
print("Until a monser attacks!")
time.sleep(0.5)
battle()

