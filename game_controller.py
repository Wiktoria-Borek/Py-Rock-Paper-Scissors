from rps_logic import get_computer_choice, determine_winner

class GameController:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0

    def play_round(self, player_choice):
        """Play a round of Rock, Paper, Scissors."""
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        self.rounds_played += 1

        # Update scores based on result
        if result == "Player Wins!":
            self.player_score += 1
        elif result == "Computer Wins!":
            self.computer_score += 1

        return player_choice, computer_choice, result

    def reset_game(self):
        """Reset the game statistics."""
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
