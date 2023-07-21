from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.xaxis=position[0]
        self.shape("square")
        self.penup()
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def down(self):
        yaxis = self.ycor()-20
        self.goto(self.xaxis, yaxis)

    def up(self):
        yaxis = self.ycor()+20
        self.goto(self.xaxis, yaxis )