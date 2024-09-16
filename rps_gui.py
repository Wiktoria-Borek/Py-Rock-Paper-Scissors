import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from rps_logic import get_computer_choice, determine_winner

class RPSGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the layout and buttons
        self.setWindowTitle("Rock, Paper, Scissors")
        layout = QVBoxLayout()

        # Label for displaying game results
        self.result_label = QLabel("Choose Rock, Paper, or Scissors to play!")
        layout.addWidget(self.result_label)

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

        # Set layout for the window
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
    
    def play(self, player_choice):
        """Handles the gameplay when the player clicks a button."""
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        self.result_label.setText(f"Player: {player_choice}, Computer: {computer_choice}\n{result}")

def main():
    app = QApplication(sys.argv)
    window = RPSGame()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
