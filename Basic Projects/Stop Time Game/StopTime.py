# Importing required modules
import time as t  # Used for tracking time
import random as r  # Used for generating random target numbers


# Define a class to manage the Stop Timer game
class StopTime:
    def __init__(self) -> None:
        """
        Initializes the StopTime object with:
        - Start time (`__st`) initialized to 0
        - End time (`__end`) initialized to 0
        - Randomly generated target number (`__num`) between 1 and 10
        """
        self.__st = 0
        self.__end = 0
        self.__num = r.choice(range(1, 11))  # Generate a random target number

    def start(self):
        """
        Starts the timer and displays the target number to the player.
        Records the start time using the `time()` function.
        """
        print(
            f"You have to stop your timer at {self.__num}"
        )  # Notify the user about the target time
        self.__st = t.time()  # Record the start time

    def stop(self):
        """
        Stops the timer by calculating the elapsed time since the start
        and calls the `res()` method to evaluate the result.
        """
        self.__end = t.time() - self.__st  # Calculate the elapsed time
        self.res()  # Call the result evaluation method

    def res(self):
        """
        Evaluates the result by comparing the elapsed time with the target number.
        - If the elapsed time (rounded) matches the target, the player wins.
        - Otherwise, displays the player's elapsed time and the target number.
        """
        if (
            round(self.__end) == self.__num
        ):  # Check if the rounded elapsed time matches the target
            print(
                f"Congrats, Your time = {round(self.__end):.2f} ; Target = {self.__num}"
            )  # Player wins
        else:
            print(
                f"Your time = {round(self.__end):.2f} ; Target = {self.__num}"
            )  # Player loses


# Create an instance of the StopTime class
stoptime = StopTime()

# Prompt the player to start the timer
choiceStart = input("Enter anything to start: ")
stoptime.start()  # Start the timer

# Prompt the player to stop the timer
choiceEnd = input("Enter anything to stop: ")
stoptime.stop()  # Stop the timer and display the result
