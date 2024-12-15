"""
paddle.py
Contient la classe Paddle pour le jeu de Pong.
"""

class Paddle:
    def __init__(self, canvas, x):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, 250, x + 20, 350, fill="white")
        self.dy = 0

    def move_up(self):
        self.dy = -5

    def move_down(self):
        self.dy = 5

    def stop(self):
        self.dy = 0

    def update(self):
        self.canvas.move(self.id, 0, self.dy)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or pos[3] >= self.canvas.winfo_height():
            self.dy = 0