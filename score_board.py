from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONTSIZE = 50


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=(FONT, FONTSIZE, "bold"))
