from turtle import Turtle, colormode
import random
colormode(255)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food_color()
        self.speed(0)
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def food_color(self):
        random_color = (random.randint(50, 255),
                        random.randint(50, 255),
                        random.randint(50, 255),
                        )
        self.color(random_color)

    def refresh(self):

        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


