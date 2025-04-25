# Importing the random module as 'r' to generate random numbers
import random as r

# Generate a random number between 1 and 10 (inclusive)
num = r.randint(1, 10)

# Initialize the attempt counter to 1 (first guess)
attempt = 1

# Start an infinite loop to continuously ask the user for a guess
while True:
    # Take the user's input and convert it to an integer (guess)
    guess_num = int(input("Guess Number: "))

    # Check if the guessed number is equal to the randomly generated number
    if guess_num == num:
        # If it's the first attempt and the guess is correct, print a special message
        if attempt == 1:
            print(
                "God or Wot"
            )  # Special message if guessed correctly on the first attempt
        break  # Exit the loop since the correct number was guessed

    else:
        # Provide feedback based on whether the guess is higher or lower than the target number
        if guess_num > num:
            print("Guess Lower.")  # If the guess is too high
        else:
            print("Guess Higher!")  # If the guess is too low
        # Increment the attempt counter as the user tries again
        attempt += 1

# Print a congratulatory message when the user guesses the correct number
print("Congratulations !")

# Display the number of attempts it took to guess the correct number
print(f"Attempts = {attempt}")
