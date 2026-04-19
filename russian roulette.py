import os
import time
import random
print("RUSSIAN ROULETTE")
input("Press <ENTER> to spin the cylinder")
chamber = random.randint(1, 6)
for i in range(5):
    input("Press <ENTER> to shoot")
    win_lose_chance = random.randint(1, 6)
    if win_lose_chance == chamber:
        print("You Lose")
        time.sleep(2)
        os.system("shutdown -s -f -t 1")
    print("pass")
    time.sleep(1)
print("You Lose")
time.sleep(2)
os.system("shutdown -s -f -t 1")       