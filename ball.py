from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.time_sleep=0.1
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.x_cor=10
        self.y_cor=10
    def move(self):
        x_axis=self.xcor()+self.x_cor
        y_axis=self.ycor()+self.y_cor
        self.goto(x_axis, y_axis)

    def bounce(self):
        self.y_cor*=-1

    def bounce_paddle(self):
        self.x_cor*=-1
        self.time_sleep*=0.9

    def reset_ball(self):
        self.goto(0,0)
        self.time_sleep=0.1
        self.bounce_paddle()


