from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.position=position
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.score=0
        self.score_vision()

    def score_vision(self):
        self.goto(self.position)
        self.write(f"score:{self.score}", align="center", font=("courier", 16, "normal"))



    def increase_score(self):
        self.score+=1
        self.clear()
        self.score_vision()