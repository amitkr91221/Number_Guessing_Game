import random
from art import logo

def play_game():
    print(logo)
    print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    number = random.randint(1,100)

    if level == 'easy':
        number_of_lives = 10
    else:
        number_of_lives = 5
    
    while number_of_lives > 0:
        guess = int(input(f"Guess the nummber\nYou have {number_of_lives} lives remaining "))
        if guess != number:
            number_of_lives -= 1
        if guess > number:
            print("Too High")
        if guess < number:
            print("Too Low")
        if guess == number:
            print("You guesses the nbumber.... You won!")
            break
        if number_of_lives == 0:
            print("You are out of live.... You lost!")


play_game()


