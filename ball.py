from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

        self.shape("circle")
        self.color("white")
        self.penup()

        self.reset_ball()

    def reset_ball(self):
        self.home()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

        heading = random.randint(-45, 45)
        if random.randint(1, 2) % 2 == 0:
            heading *= -1
        self.setheading(heading)

    def move_ball(self):
        self.forward(4)

    def change_direction(self, new_head):
        # self.move_speed *= 0.9
        self.setheading(new_head)
