import random
import time

posible_nums = list(range(1, 101))
continue_playing = True
guessed_numbers = []

print("Pick a number between 1 and 100.")
start = input("Do you have one?")

while continue_playing == True:
    guess = int(random.choice(posible_nums))
    if int(guess) in guessed_numbers:
        continue
    else:
        print("I think " + str(guess) + " is your number.")
        time.sleep(1)
        ans = input("Is it your number? [y/n]")
        if ans == "y":
            print("Yay!")
            continue_playing = False
        else:
            guessed_numbers.append(guess)
            higher = input("Is your number higher? [y/n]")
            if higher == "y":
                posible_nums = list(range(guess, posible_nums[-1]+1))
            else:
                print("Your number must be lower...")
                posible_nums = list(range(posible_nums[0], guess + 1))