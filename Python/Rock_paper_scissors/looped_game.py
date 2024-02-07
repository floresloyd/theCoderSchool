import random

# ASCII Art for Rock, Paper, Scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Dictionary to hold the ASCII art
game_art = {"rock": rock, "paper": paper, "scissors": scissors}

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

# Main game function
def play_game():
    player_wins = 0
    computer_wins = 0

    while player_wins < 2 and computer_wins < 2:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        while player_choice not in ["rock", "paper", "scissors"]:
            player_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()

        computer_choice = get_computer_choice()

        print("\nYour choice:")
        print(game_art[player_choice])

        print("\nComputer's choice:")
        print(game_art[computer_choice])

        winner = determine_winner(player_choice, computer_choice)
        if winner == "player":
            player_wins += 1
            print("\nYou win this round!")
        elif winner == "computer":
            computer_wins += 1
            print("\nComputer wins this round!")
        else:
            print("\nThis round is a tie!")

        print(f"Score: You - {player_wins}, Computer - {computer_wins}\n")

    if player_wins > computer_wins:
        print("Congratulations! You won the best of three match!")
    else:
        print("Game over. The computer won the best of three match.")

# Start the game
play_game()
