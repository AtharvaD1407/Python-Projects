class ATM:
    def __init__(self, bal) -> None:
        """
        Initialize the ATM object with a balance.

        Args:
        bal (int): The initial balance in the ATM account.
        """
        self.__balance = bal  # Private variable to store the balance.

    def withdraw(self, amount):
        """
        Process a withdrawal from the ATM account.

        Args:
        amount (int): The amount to be withdrawn.

        If the amount is greater than the current balance, an error is shown.
        Otherwise, the balance is reduced by the withdrawal amount.
        """
        if amount > self.__balance:
            print(
                "Insufficient funds!"
            )  # Show an error if the balance is insufficient.
        else:
            self.__balance -= amount  # Deduct the withdrawal amount from the balance.
            print(
                f"Withdrawal successful! Remaining balance: {self.__balance}"
            )  # Display updated balance.

    def deposit(self, amount):
        """
        Deposit an amount into the ATM account.

        Args:
        amount (int): The amount to be deposited.

        The balance is increased by the deposit amount.
        """
        self.__balance += amount  # Increase the balance by the deposit amount.
        print(
            f"Deposit successful! Updated balance: {self.__balance}"
        )  # Display updated balance.

    def checkBalance(self):
        """
        Get the current balance of the ATM account.

        Returns:
        int: The current balance.
        """
        return self.__balance  # Return the current balance.


def get_valid_input(prompt, valid_choices):
    """
    Prompt the user for input and validate that it is a valid choice.

    Args:
    prompt (str): The message to be displayed to the user.
    valid_choices (list): A list of valid options for the user to select.

    Returns:
    int: The validated user input.
    """
    while True:
        try:
            user_input = int(input(prompt))  # Get user input as an integer.
            if user_input not in valid_choices:
                print(
                    f"Please choose a valid option from {valid_choices}."
                )  # Check if input is in valid choices.
            else:
                return user_input  # Return the valid user input.
        except ValueError:
            print(
                "Invalid input. Please enter a number."
            )  # Handle case where input is not a valid number.


# Get the initial balance from the user
try:
    userBal = int(
        input("Enter your initial balance: ")
    )  # Get the initial balance from the user.
except ValueError:
    print(
        "Invalid balance input. Please enter a valid number."
    )  # Handle invalid balance input.
    exit()  # Exit the program if the balance is invalid.

# Create an ATM object with the initial balance
atm = ATM(userBal)

# Start the loop for user interaction
while True:
    # Display the ATM menu and get the user's choice
    userChoice = get_valid_input(
        """\nEnter:
        1. Withdraw 
        2. Deposit
        3. Check Balance
        4. Exit
        Choose an option: """,
        [1, 2, 3, 4],  # Valid options for the user.
    )

    if userChoice == 1:  # If the user selects "Withdraw" option
        try:
            amount = int(
                input("Enter amount to withdraw: ")
            )  # Get the withdrawal amount.
            if amount <= 0:
                print(
                    "Amount must be greater than 0."
                )  # Ensure that the withdrawal amount is positive.
            else:
                atm.withdraw(amount)  # Call the withdraw method of ATM object.
        except ValueError:
            print(
                "Invalid amount entered. Please enter a number."
            )  # Handle invalid withdrawal amount input.

    elif userChoice == 2:  # If the user selects "Deposit" option
        try:
            amount = int(input("Enter amount to deposit: "))  # Get the deposit amount.
            if amount <= 0:
                print(
                    "Amount must be greater than 0."
                )  # Ensure that the deposit amount is positive.
            else:
                atm.deposit(amount)  # Call the deposit method of ATM object.
        except ValueError:
            print(
                "Invalid amount entered. Please enter a number."
            )  # Handle invalid deposit amount input.

    elif userChoice == 3:  # If the user selects "Check Balance" option
        print(
            f"Your current balance is: {atm.checkBalance()}"
        )  # Display the current balance.

    elif userChoice == 4:  # If the user selects "Exit" option
        print(
            "Thank you for using our ATM service!"
        )  # Show a farewell message and exit the loop.
        break  # Exit the loop and end the program.
