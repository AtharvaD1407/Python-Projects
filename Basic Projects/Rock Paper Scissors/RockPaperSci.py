import random as r


# Function for two-player mode
def twoPlayer(arr, player1, player2):
    p1_score, p2_score = 0, 0  # Initialize scores

    # Loop for a best-of-3 game
    for i in range(3):
        print(f"Round {i + 1}:")
        print(f"{player1}'s Turn:")
        p1_choice = input("Enter R for Rock, P for Paper, S for Scissor: ").lower()

        print(f"{player2}'s Turn:")
        p2_choice = input("Enter R for Rock, P for Paper, S for Scissor: ").lower()

        # Determine the winner of the round
        if p1_choice == p2_choice:
            print("It's a tie!")
        elif (
            (p1_choice == "r" and p2_choice == "s")
            or (p1_choice == "p" and p2_choice == "r")
            or (p1_choice == "s" and p2_choice == "p")
        ):
            p1_score += 1
            print(f"{player1} wins this round!")
        else:
            p2_score += 1
            print(f"{player2} wins this round!")

        # Check if someone has won 2 rounds
        if p1_score == 2:
            print(f"{player1} wins the game!")
            break
        elif p2_score == 2:
            print(f"{player2} wins the game!")
            break

    # If all rounds are played and no one has won 2 rounds
    if p1_score == p2_score:
        print("The game ends in a tie!")
    elif p1_score > p2_score:
        print(f"{player1} wins with a score of {p1_score} to {p2_score}!")
    else:
        print(f"{player2} wins with a score of {p2_score} to {p1_score}!")


# Function for playing against the computer
def vsComp(arr):
    comp_score, user_score = 0, 0  # Initialize scores

    # Loop for a best-of-3 game
    for i in range(3):
        comp = r.choice(list(arr.values()))  # Random computer choice
        print(f"Round {i + 1}:")

        print("Computer Choose.")
        user = input(
            "Your Turn (Enter R for Rock, P for Paper, S for Scissor): "
        ).lower()

        # Determine the winner of the round
        if user == comp:
            print("It's a tie!")
        elif (
            (comp == "r" and user == "s")
            or (comp == "p" and user == "r")
            or (comp == "s" and user == "p")
        ):
            comp_score += 1
            print("Computer wins this round!")
        else:
            user_score += 1
            print("You win this round!")

        # Check if someone has won 2 rounds
        if comp_score == 2:
            print("Computer wins the game!")
            break
        elif user_score == 2:
            print("You win the game!")
            break

    # If all rounds are played and no one has won 2 rounds
    if comp_score == user_score:
        print("The game ends in a tie!")
    elif comp_score > user_score:
        print(f"Computer wins with a score of {comp_score} to {user_score}!")
    else:
        print(f"You win with a score of {user_score} to {comp_score}!")


# Main program
print("Welcome to Rock, Paper, Scissors!")
print(
    """
It'll be Best of 3.
First to win 2 rounds wins the game.

Enter R - Rock, P - Paper, S - Scissor.
"""
)

# Mapping for choices
arr = {"Rock": "r", "Paper": "p", "Scissor": "s"}

# Prompt the user to choose game mode
choice = int(input("Choose Game Mode: 1-Computer, 2-Two Player: "))
match choice:
    case 1:
        vsComp(arr)
    case 2:
        player1 = input("Name of Player 1: ")
        player2 = input("Name of Player 2: ")
        twoPlayer(arr, player1, player2)
    case _:
        print("Invalid Input. Exiting.")
