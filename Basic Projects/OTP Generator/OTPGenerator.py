# Importing necessary modules:
# 'random' for generating random numbers, and 'math' for using the 'floor' function
import random as r
import math as m

# Function to generate OTP (One-Time Password)
# 'len' is the length of the OTP the user wants
def generateOTP(len):
    otp = ""  # Initialize an empty string to store the OTP

    # Loop to generate each digit of the OTP
    for i in range(len):
        # Generate a random floating-point number between 0 and 1
        # Multiply by 10 to scale it to a range of 0-9, then use 'floor' to round down to an integer
        num = m.floor(r.random() * 10)
        
        # Convert the generated number to a string and append it to the OTP
        otp += str(num)

    # Return the OTP as an integer (not a string)
    return int(otp)

# Taking input from the user to define the length of the OTP
otp_length = int(input("Enter the length of OTP: "))

# Calling the function and printing the generated OTP
print(generateOTP(otp_length))
