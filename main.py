from turtle import getscreen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score_bord import ScoreBoard


def border():
    middle_line = Turtle()
    middle_line.speed(0)
    middle_line.penup()
    middle_line.color("white")
    middle_line.goto(0, -280)
    middle_line.left(90)
    while True:
        middle_line.pendown()
        middle_line.fd(40)
        middle_line.penup()
        middle_line.fd(20)
        if middle_line.ycor() > 280:
            break


border()
my_screen = getscreen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = ScoreBoard((200, 270))
l_score = ScoreBoard((-200, 270))

my_screen.listen()
my_screen.onkey(r_paddle.down, "Down")
my_screen.onkey(r_paddle.up, "Up")
my_screen.onkey(l_paddle.down, "s")
my_screen.onkey(l_paddle.up, "w")
is_move = True
score = 0
while is_move:

    ball.move()
    time.sleep(ball.time_sleep)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset_ball()
        l_score.increase_score()
        print(score)
    elif ball.xcor() < -380:
        ball.reset_ball()
        r_score.increase_score()
    my_screen.update()

my_screen.exitonclick()
