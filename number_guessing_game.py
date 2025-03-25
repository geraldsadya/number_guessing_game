import random
import time

def display_welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it within the given number of attempts.")
    print()

def select_difficulty():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                chances = 10
                print("\nGreat! You have selected the Easy difficulty level.")
                break
            elif choice == 2:
                chances = 5
                print("\nGreat! You have selected the Medium difficulty level.")
                break
            elif choice == 3:
                chances = 3
                print("\nGreat! You have selected the Hard difficulty level.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print("Let's start the game!")
    return chances

def play_game():

def play_again():

def main():
