"""
interface.py
Contient la classe PongInterface qui gère l'interface utilisateur du jeu.
"""

import tkinter as tk

class PongInterface:
    def __init__(self, game):
        self.root = tk.Tk()
        self.root.title("Pong Game")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.root.bind("<KeyPress>", game.key_press)
        self.root.bind("<KeyRelease>", game.key_release)

    def run(self):
        self.root.mainloop()

    def after(self, delay, callback):
        self.root.after(delay, callback)