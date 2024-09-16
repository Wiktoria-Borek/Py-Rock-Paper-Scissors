import random

# Game choices
choices = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    """Randomly selects the computer's choice."""
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determines the winner of the game."""
    if player_choice == computer_choice:
        return "Draw"
    
    if (player_choice == "Rock" and computer_choice == "Scissors") or \
       (player_choice == "Paper" and computer_choice == "Rock") or \
       (player_choice == "Scissors" and computer_choice == "Paper"):
        return "Player Wins!"
    
    return "Computer Wins!"
