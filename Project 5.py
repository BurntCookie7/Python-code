import sys

#define vars
answer = None
score = 0

#Question 1
print("Are you living?")
answer = input()

if answer == "yes":
    print("Correct!\n")
    score = score +1
elif answer == "Yes":
    print("Correct!\n")
    score = score +1
elif answer == "Yes.":
    print("Correct!\n")
    score = score +1
else:
    print("Wrong!\n")

#Question 2
print("Is the Earth spinning?")
answer = input()

if answer == "yes":
    print("Correct!\n")
    score = score +1
elif answer == "Yes":
    print("Correct!\n")
    score = score +1
elif answer == "Yes.":
    print("Correct!\n")
    score = score +1
else:
    print("Wrong!\n")

#Question 3
print("is the sky blue?")
answer = input()

if answer == "yes":
    print("Correct!\n")
    score = score +1
elif answer == "Yes":
    print("Correct!\n")
    score = score +1
elif answer == "Yes.":
    print("Correct!\n")
    score = score +1
else:
    print("Wrong!\n")

#show score
print()
if score == 0:
    print("You had to be trying to get everything that wrong")
if score == 1:
    print("Not terrible I guess...")
if score == 2:
    print("Good job!")
