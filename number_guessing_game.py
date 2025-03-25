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
    display_welcome()
    chances = select_difficulty()
    
    target_number = random.randint(1, 100)
    attempts = 0

    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            if guess == target_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                return True
            elif guess < target_number:
                print("Incorrect! The number is greater than your guess.")
            else:
                print("Incorrect! The number is less than your guess.")
            remaining = chances - attempts
            if remaining > 0:
                print(f"You have {remaining} chances left.")            
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame Over! You've run out of chances. The number was {target_number}.")
    return False

def play_again():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    while True:
        play_game()
        if not play_again():
            print("\nThank you for playing the Number Guessing Game. Goodbye!")
            break

if __name__ == "__main__":
    main()
