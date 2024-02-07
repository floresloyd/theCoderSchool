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
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        #return "You win!"
        return "You scored a point!"
    else:
        #return "You lose!"
        return "Computer scores a point!"
# Main game function
def play_game():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()

    computer_choice = get_computer_choice()

    print("\nYour choice:")
    print(game_art[player_choice])

    print("\nComputer's choice:")
    print(game_art[computer_choice])

    print("\nResult:")
    print(determine_winner(player_choice, computer_choice))

# Start the game


play_game()
