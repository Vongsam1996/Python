#Here is a random number Generator from 1 to 10
import random
#This is a random number generator that generates a random number between 1 and 10

def Guessing_game():
#random.ranint = random integer within the range of (x to y)
    Guessed_number = random.randint(1, 30)
    guess = None
    attempts = 0
    #attempts will count how much attempts the player made

    print("Guess a number between 1 and 30")

#We want to Loop until the user guesses the correct number
    while guess != Guessed_number:
        attempts += 1

#User input
        guess = int(input("Enter your guess: "))
#int = integer

        if guess < Guessed_number:
            print("Too low! Try again.")
        elif guess > Guessed_number:
            print("Too high! Try again.")
        else:
            print("Nice! You are correct", attempts, "attempts.")
Guessing_game()
#This is a function that will run the guessing game