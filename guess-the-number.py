import random

print("Guess the number from 1 to 20! You have 7 attempts to guess it right.")

while True:
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Write your guess: "))

        attempts += 1

        if attempts > 7:
            print(f"Sorry, you've used all your attempts! The secret number was {secret_number}.")
            break

        if guess < secret_number:
            print("Your guess is less than the secret number. Try again!")
        elif guess > secret_number:
            print("Your guess is greater than the secret number. Try again!")
        else:
            print(f"Great job! You guessed the secret number {secret_number} in {attempts} attempts!")
            break

    play_again = input("Would you like to play again? (yes/no) ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
