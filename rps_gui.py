import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from game_controller import GameController

class RPSGame(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = GameController()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Rock, Paper, Scissors")
        layout = QVBoxLayout()

        # Label for displaying game results
        self.result_label = QLabel("Choose Rock, Paper, or Scissors to play!")
        layout.addWidget(self.result_label)

        # Label for displaying scores
        self.score_label = QLabel(f"Player: 0 | Computer: 0 | Rounds: 0")
        layout.addWidget(self.score_label)

        # Create buttons for each choice
        self.rock_button = QPushButton("Rock", self)
        self.rock_button.clicked.connect(lambda: self.play("Rock"))
        layout.addWidget(self.rock_button)

        self.paper_button = QPushButton("Paper", self)
        self.paper_button.clicked.connect(lambda: self.play("Paper"))
        layout.addWidget(self.paper_button)

        self.scissors_button = QPushButton("Scissors", self)
        self.scissors_button.clicked.connect(lambda: self.play("Scissors"))
        layout.addWidget(self.scissors_button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def play(self, player_choice):
        """Handles the gameplay when the player clicks a button."""
        player_choice, computer_choice, result = self.controller.play_round(player_choice)
        self.result_label.setText(f"Player: {player_choice}, Computer: {computer_choice}\n{result}")
        self.update_score()

    def update_score(self):
        """Updates the score and round labels."""
        self.score_label.setText(
            f"Player: {self.controller.player_score} | "
            f"Computer: {self.controller.computer_score} | "
            f"Rounds: {self.controller.rounds_played}"
        )

