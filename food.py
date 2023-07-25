from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")             # To make the food a circle
        self.penup()                     # To prevent anything from being written when the food moves and only display it at the point where it appears
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # To reduce its size by half
        self.color("blue")               # To make the food blue
        self.speed("fastest")            # To make the food move immediately and not show any animation
        self.refresh()                   # Call the random food function

    # To make the food appear at a random position within the range (up to 300 in X and 300 in Y).
    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)