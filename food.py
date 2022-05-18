from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """
        create the food
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        every time the refresh function is called,
        the food will go to its original place
        """
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(x=random_x, y=random_y)