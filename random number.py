import random

def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    print("I am thinking of a number between 1 and 100. Can you guess it?")
    
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  # To count the number of guesses
    
    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
