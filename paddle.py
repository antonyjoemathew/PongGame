from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def change_position(self, positon):
        self.goto(positon)

    def move_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        new_y = min(new_y, 250)

        self.change_position((new_x, new_y))

    def move_down(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        new_y = max(new_y, -250)
        self.change_position((new_x, new_y))
