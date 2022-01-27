"""
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
2. On a player's first turn, if their guess is
    .within 10 of the number, return "WARM!"
    .further than 10 away from the number, return "COLD!"
3. On all subsequent turns, if a guess is
    .closer to the number than the previous guess return "WARMER!"
    .farther from the number than the previous guess, return "COLDER!"
4. When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
"""

from random import randint

num = randint(1, 100)
gusse_list = []
while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    gusse_list.append(guess)

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(gusse_list)} GUESSES!!')
        break

    if len(gusse_list) == 1:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(num - gusse_list[-2]) < abs(num - guess):
            print("COLDER!")
        else:
            print("WARMER!")