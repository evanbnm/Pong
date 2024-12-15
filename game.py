"""
game.py
Contient la classe PongGame qui gère la logique du jeu.
"""

from interface import PongInterface
from ball import Ball
from paddle import Paddle

class PongGame:
    def __init__(self):
        self.interface = PongInterface(self)
        self.ball = None
        self.paddle1 = None
        self.paddle2 = None
        self.game_started = False

    def key_press(self, event):
        if not self.game_started:
            self.start_game()
        else:
            if event.keysym == "z":
                self.paddle1.move_up()
            elif event.keysym == "s":
                self.paddle1.move_down()
            elif event.keysym == "Up":
                self.paddle2.move_up()
            elif event.keysym == "Down":
                self.paddle2.move_down()

    def key_release(self, event):
        if self.game_started:
            if event.keysym in ("z", "s"):
                self.paddle1.stop()
            elif event.keysym in ("Up", "Down"):
                self.paddle2.stop()

    def show_start_screen(self):
        self.interface.canvas.create_text(400, 300, text="Appuyez sur une touche pour commencer", fill="white", font=("Helvetica", 24))
        self.interface.root.bind("<KeyPress>", self.key_press)

    def start_game(self):
        self.game_started = True
        self.interface.canvas.delete("all")
        self.ball = Ball(self.interface.canvas)
        self.paddle1 = Paddle(self.interface.canvas, x=30)
        self.paddle2 = Paddle(self.interface.canvas, x=770)
        self.interface.root.bind("<KeyPress>", self.key_press)
        self.interface.root.bind("<KeyRelease>", self.key_release)
        self.run()

    def run(self):
        if self.game_started:
            self.update()
        self.interface.run()

    def update(self):
        if self.game_started:
            self.ball.move()
            self.paddle1.update()
            self.paddle2.update()
            self.interface.after(20, self.update)