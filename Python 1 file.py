import random
import time
import sys
c = random.randint(1, 6)
print("Russian Roulette!")
for i in range(5):
    input("press enter to shoot")
    b = random.randint(1, 6)
    if b == c:
        print("You Lose!")
        sys.exit(SystemExit)
print("You Win!")
