"""
Guessing Game Challenge
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
"""

import random
x = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")


number_of_guesses = [0]


while True:
    guess = int(input("What's your guess? "))
    if guess < 1 or guess > 100:
        print("out of bounds")
        continue
    number_of_guesses.append(guess)
    if guess == x:
        print ("Perfect. You tried {} times".format(len(number_of_guesses)))
        break    
    elif abs(guess-x) > 10:
        print(guess, "is cold")
    elif abs(guess-x) <= 2:
        print(guess, "is hot")
    elif abs(guess-x) <= 5:
        print(guess, "is warmer")
    elif abs(guess-x) <= 10:
        print(guess, "is warm")
