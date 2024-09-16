from PyQt5.QtWidgets import QApplication
import sys
from rps_gui import RPSGame

def main():
    app = QApplication(sys.argv)
    game = RPSGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
