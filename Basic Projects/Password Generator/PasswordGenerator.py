import random
import string


def generate_password(strength, length=8):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Choose character set based on strength level
    if strength == "weak":
        char_pool = lowercase
    elif strength == "medium":
        char_pool = lowercase + uppercase + digits
    elif strength == "strong":
        char_pool = lowercase + uppercase + digits + symbols
    elif strength == "very strong":
        char_pool = lowercase + uppercase + digits + symbols
        length = max(
            12, length
        )  # Ensure very strong passwords are at least 12 characters
    else:
        return "Invalid strength level. Choose from weak, medium, strong, very strong."

    # Generate password
    password = "".join(random.choice(char_pool) for _ in range(length))
    return password


# Get user input
strength = input("Enter password strength (weak/medium/strong/very strong): ").lower()
length = int(input("Enter password length: "))

# Generate and display password
print(f"Generated {strength} password: {generate_password(strength, length)}")
