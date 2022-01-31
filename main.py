from art import logo
import random


def play():
    print(logo)
    computer_choice = random.randint(1, 100)
    game_difficulty = input("Please choose difficulty - Easy or Hard: ").lower()
    if game_difficulty == "easy":
        lives = 10
        guess(computer_choice, lives)
    elif game_difficulty == "hard":
        lives = 5
        guess(computer_choice, lives)
    else:
        print("You entered an invalid response")
        wanna_play()

# Function to play easy mode
def guess(computer_choice, lives):
    print(f"You have {lives} lives to guess the number!")
    while lives != 0:
        guess = int(input("Please guess a number between 1 and 100 "))
        if guess == computer_choice:
            print(f"Well done! You got it right, you win a medal! Computer chose {computer_choice}")
            wanna_play()
        elif guess < computer_choice:
            lives -= 1
            print(f"Too low! You have {lives} lives left")
        elif guess > computer_choice:
            lives -= 1
            print(f"Too high! You have {lives} lives left")
    if lives == 0:
        print(f"You have run out of lives. The number was {computer_choice}")
        wanna_play()

# Asking if the user would like to play
def wanna_play():
    user_play = input("Would you like to play the number guessing game? Type 'y' for yes and 'n' for no: ").lower()
    if user_play == "y":
        play()
    elif user_play == "n":
        print("OK, Goodbye!")
        quit()
    else:
        print("You entered an invalid response, Good bye")
        quit()

wanna_play()