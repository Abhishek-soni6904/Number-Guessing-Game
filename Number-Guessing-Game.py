from random import randint

def get_range_input():
    """
    Prompts the user to enter the start and end values for the guessing range.
    Ensures the input is valid and returns the range as a tuple.
    """
    while True:
        try:
            min_value = int(input("🔢 Enter the starting value for the range: "))
            max_value = int(input("🔢 Enter the ending value for the range: "))
            if min_value >= max_value:
                print("❌ The starting value must be less than the ending value. Please try again.\n")
            else:
                return min_value, max_value
        except ValueError:
            print("🚫 Invalid input. Please enter numeric values.\n")


def get_user_guess(previous_guesses):
    """
    Prompts the user to enter a guess. Ensures the input is valid and returns the guess.
    """
    while True:
        try:
            if previous_guesses:
                print(f"📜 Previous guesses: {previous_guesses}")
            guess = int(input("💭 Enter your guess: "))
            return guess
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.\n")


def validate_guess(guess, min_value, max_value, target_number, previous_guesses):
    """
    Validates the user's guess and provides feedback.
    Returns True if the guess is correct, False otherwise.
    """
    if guess < min_value or guess > max_value:
        print(f"⚠️  Please enter a number between {min_value} and {max_value}.")
        return True
    elif guess in previous_guesses:
        print("🔄 This number has already been guessed. Please try a different number.")
        return False
    elif guess > target_number:
        print("📉 Your guess is higher than the target. Try a lower number.")
        return True
    elif guess < target_number:
        print("📈 Your guess is lower than the target. Try a higher number.")
        return True
    else:
        return True   

def ask_for_rematch():
    """
    Asks the user if they want to play another round.
    Returns True for 'yes' and False for 'no'.
    """
    while True:
        user_input = input("\n🔄 Play another round? Enter [y/n]: ").lower()
        if user_input == 'y':
            print("\n🔥 Starting a new game...\n")
            return True
        elif user_input == 'n':
            print("\n🎉 Thanks for playing! See you next time.")
            return False
        else:
            print("❌ Invalid input. Please enter 'y' for yes or 'n' for no.")


def play_game():
    """
    Main game loop that runs the Number Guessing Game.
    """
    print("🎲 Welcome to the Number Guessing Game!")
    
    # Get valid range from the user
    min_value, max_value = get_range_input()

    # Set the target number and initialize variables
    target_number = randint(min_value, max_value)
    previous_guesses = []
    attempts = 1

    print("\n🚀 Game has started! Try to guess the number.\n")

    # Main guessing loop
    while True:
        print(f"🔢 Attempt {attempts}:")
        guess = get_user_guess(previous_guesses)

        if validate_guess(guess, min_value, max_value, target_number, previous_guesses):
            previous_guesses.append(guess)
        if(guess==target_number):    
            print(f"\n🎯 Congratulations! You guessed the correct number {target_number}!")
            attempt_word = "attempt" if attempts == 1 else "attempts"
            print(f"🏆 It took you {attempts} {attempt_word}.")
            print(f"📜 Your guesses: {previous_guesses}")
            break
        attempts += 1

def start_game():
    """
    Starts the game and manages the rematch functionality.
    """
    while True:
        play_game()
        if not ask_for_rematch():
            break


if __name__ == "__main__":
    start_game()