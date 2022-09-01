from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("#000000")
screen.tracer(0)
screen.title("Pong")
paddle_right = Paddle()
paddle_right.change_position((int(screen.window_width() / 2) - 20, 0))
paddle_left = Paddle()
paddle_left.change_position((int(-1 * screen.window_width() / 2) + 10, 0))
ball = Ball()
score_left = ScoreBoard((-1 * screen.window_width() / 4, screen.window_height() / 2 - 80))
score_right = ScoreBoard((screen.window_width() / 4, screen.window_height() / 2 - 80))

screen.listen()
screen.onkey(fun=paddle_right.move_up, key="Up")
screen.onkey(fun=paddle_right.move_down, key="Down")

screen.onkey(fun=paddle_left.move_up, key="q")
screen.onkey(fun=paddle_left.move_down, key="a")

is_game_on = True


def is_ball_hit_the_paddles():
    if ball.distance(paddle_left) < 50 and ball.xcor() <= (paddle_left.xcor() + 20):
        print("is_ball_hit_the_ left paddles")
        return True
    elif ball.distance(paddle_right) < 50 and ball.xcor() >= (paddle_right.xcor() - 20):
        print("is_ball_hit_the_ rightpaddles")
        return True
    # ball.setheading((-1 * ball.heading()) % 360)

    return False


def is_ball_hit_the_side_wall():
    if ball.xcor() <= (paddle_left.xcor()):
        print("right one point")
        score_right.update_score()
        return True
    elif ball.xcor() >= (paddle_right.xcor()):
        print("left one point")
        score_left.update_score()
        return True
    return False


def is_ball_hit_top_or_bottom():
    dist = 20
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        print("hit the top or bottom")
        return True
    return False


while is_game_on:
    screen.update()
    # time.sleep(0.03)
    ball.move_ball()
    if is_ball_hit_top_or_bottom():
        ball.change_direction((-1 * ball.heading()) % 360)
    if is_ball_hit_the_paddles():
        ball.change_direction((180 - ball.heading()) % 360)
    elif is_ball_hit_the_side_wall():
        ball.reset_ball()
        time.sleep(0.5)

screen.exitonclick()
