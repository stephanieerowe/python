# Number Guessing Game

# The program picks a random number between 1 and 100. The user keeps guessing until they get it right.

# 🔧 Practice: loops, conditionals, input/output, random module.


import random 
import time

# Function to start the game
def start_game():
    print("Game is starting...")
    time.sleep(1.5) # two second delay

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while True:
        userReady = input("Are you ready to begin the number guessing game? Type yes or no: ").lower()
        if userReady == "yes":
            break
        elif userReady == "no":
            print("Okay, I'll ask again later...")
            time.sleep(5)
        else:
            print("I said type yes or no. You're not very good at reading, are you...")


    while not guessed:
        user_guess = int(input("Enter your guess!: "))

        if user_guess > number_to_guess:
            print("Too high")
        elif user_guess < number_to_guess:
            print("Too low")
        else:
            print("Correct! The number was " + str(number_to_guess) + ". You guessed the number in " + str(attempts) + " attempts.")
            guessed = True
            return
                
        attempts+=1

while True:
    start_game()
    replay = input("Do you want to play again? Type yes or no: ").lower()
    if replay != "yes":
        print("Thanks for playing! Goodbye!")
        break
            



