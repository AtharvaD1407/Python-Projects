import random as r

# Dictionary of words with their hints
words = {
    "Variable": "A placeholder for storing data values in programming.",
    "Function": "A block of reusable code that performs a specific task.",
    "Loop": "A control structure that repeatedly executes a block of code.",
    "List": "A collection of ordered, changeable, and indexed elements.",
    "Dictionary": "A collection of key-value pairs used to store data.",
    "String": "A sequence of characters enclosed in quotes.",
    "Integer": "A whole number, positive or negative, without decimals.",
    "Module": "A file containing Python code that can be imported and reused.",
    "Class": "A blueprint for creating objects in object-oriented programming.",
    "Object": "An instance of a class in object-oriented programming.",
    "Syntax": "The set of rules that define the structure of a programming language.",
    "Exception": "An error that occurs during the execution of a program.",
    "Indentation": "The use of spaces or tabs to structure code in Python.",
    "Comment": "A note in the code ignored by the compiler or interpreter.",
    "Library": "A collection of prewritten code for common tasks in programming.",
    "Compile": "The process of converting source code into machine code.",
    "Debugging": "The process of finding and fixing errors in code.",
    "API": "A set of rules for communication between software applications.",
    "Framework": "A pre-built structure for developing software applications.",
    "Script": "A small program written to automate simple tasks.",
}

# Choose a random word and its corresponding hint
randWord, hint = r.choice(list(words.items()))
randWord = (
    randWord.lower()
)  # Convert the word to lowercase for case-insensitive comparison

# Display the hint to the user
print(f"Hint: {hint}")

# Create a list of blanks to represent the word
blanks = list("_" * len(randWord))  # Each "_" corresponds to a letter in the word

# Start the game loop
while True:
    # Show the current state of the word with blanks and guessed letters
    print("Word: " + "".join(blanks))

    # Ask the user to guess a letter
    letter = input(
        "Guess the letter: "
    ).lower()  # Convert input to lowercase for case-insensitivity

    # Check if the guessed letter matches any letter in the random word
    for i, j in enumerate(randWord):  # Loop through each letter in the word
        if j == letter:  # If the guessed letter matches the current letter
            blanks[i] = letter  # Replace the blank with the guessed letter

    # Check if the word is fully guessed
    if "".join(blanks) == randWord:
        print(f"Congratulations! You guessed the word: {randWord}")  # Success message
        break  # Exit the loop and end the game
