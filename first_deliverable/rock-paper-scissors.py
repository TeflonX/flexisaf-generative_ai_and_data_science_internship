from random import randint

# Constants
ROCK = 1
PAPER = 2
SCISSORS = 3
EXIT = 0

CHOICES = {
    ROCK: "Rock",
    PAPER: "Paper",
    SCISSORS: "Scissors"
}

WINNING_MOVES = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}


def display_choices(player_choice, computer_choice):
    """Display both player and computer selections."""
    
    print(f"\nYou played: {CHOICES[player_choice]}")
    print(f"Computer played: {CHOICES[computer_choice]}")


def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""

    if player_choice == computer_choice:
        return "draw"

    if WINNING_MOVES[player_choice] == computer_choice:
        return "player"

    return "computer"


def get_player_choice():
    """Get and validate user input."""

    try:
        choice = int(
            input(
                "\nType 1 for Rock, 2 for Paper, 3 for Scissors or 0 to Exit: "
            )
        )

        if choice not in [0, 1, 2, 3]:
            print("Invalid input. Please enter 0, 1, 2, or 3.")
            return None

        return choice

    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    while True:
        player_choice = get_player_choice()

        if player_choice is None:
            continue

        if player_choice == EXIT:
            print("Thanks for playing!")
            break

        computer_choice = randint(1, 3)

        display_choices(player_choice, computer_choice)

        result = determine_winner(player_choice, computer_choice)

        if result == "draw":
            print("Stalemate! Play again.")
        elif result == "player":
            print("You win!")
        else:
            print("Computer wins!")


if __name__ == "__main__":
    main()