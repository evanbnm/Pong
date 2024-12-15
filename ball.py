"""
ball.py
Contient la classe Ball pour le jeu de Pong.
"""

class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(390, 290, 410, 310, fill="white")
        self.dx = 3
        self.dy = 3

    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or pos[3] >= self.canvas.winfo_height():
            self.dy = -self.dy
        if pos[0] <= 0 or pos[2] >= self.canvas.winfo_width():
            self.dx = -self.dx

        # Vérification des collisions avec les paddles
        self.check_collision()

    def check_collision(self):
        pos = self.canvas.coords(self.id)
        items = self.canvas.find_overlapping(pos[0], pos[1], pos[2], pos[3])
        for item in items:
            if item != self.id:
                self.dx = -self.dx
                break