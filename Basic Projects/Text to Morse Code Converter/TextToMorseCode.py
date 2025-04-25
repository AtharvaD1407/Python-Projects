# Data dictionary containing the mapping of characters to their Morse code equivalents
data = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "Error": "........",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "x": "-..-",
    "%": "----- -..-. -----",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    " ": "/",  # Space is represented by '/' in Morse code
}


# Function to convert a user-provided message to Morse code
def converter():
    # Prompt the user to enter their message
    userStr = input(
        "Enter your message: "
    ).upper()  # Convert the input to uppercase for consistency

    # Loop through each character in the input message
    for i in userStr:
        # Fetch and print the corresponding Morse code from the dictionary
        # Print the Morse code with a space separating each character's code
        print(data[i], end=" ")

    # Ask the user if they want to convert another message
    toConti = input("\nWant to continue: (y/n) ").lower()

    # If the user chooses 'n', exit the function
    if toConti == "n":
        return

    # Recursively call the converter function to continue
    converter()


# Entry point of the program
if __name__ == "__main__":
    converter()  # Start the Morse code conversion process
