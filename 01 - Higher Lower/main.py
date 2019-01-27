import random

num = random.randint(1, 100)

while (True):
    choice = int(input("> "))

    if (choice is num):
        print("You win. It is", num)
        break
    if (choice > num):
        print("Lower")
    if (choice < num):
        print("Higher")
