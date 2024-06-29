# import modules
import random

# create loop

keepLooping = True
while keepLooping:
    try:
        upper_limit = int(input("Level: "))
        num = random.randint(1, upper_limit)
        guess = int(input("Guess: "))

        if num < guess:
            print("too large!")

        elif num > guess:
            print("too small!")

        elif num == guess:
            print("just right!")
            keepLooping = False

    except ValueError:
        continue

