import random

posible_nums = list(range(1, 101))
continue_playing = True
guessed_numbers = []

print("Pick a number between 1 and 100.")
start = input("Do you have one?")

while continue_playing == True:
    guess = int(random.choice(posible_nums))
    if int(guess) in guessed_numbers:
        print("Already guessed")
        continue
    else:
        print("I think " + str(guess) + " is your number.")
        ans = input("Is it your number?")
        if ans == "y":
            print("Yay!")
            continue_playing = False
        else:
            guessed_numbers.append(guess)
            higher = input("Is your number higher?")
            if higher == "y":
                posible_nums = list(range(guess, posible_nums[-1]+1))
            else:
                lower = input("Is your number lower?")
                if lower == "y":
                    posible_nums = list(range(posible_nums[0], guess + 1))