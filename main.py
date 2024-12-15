"""
main.py
Point d'entrée du jeu de Pong.
"""

from game import PongGame

if __name__ == "__main__":
    game = PongGame()
    game.show_start_screen()
    game.run()