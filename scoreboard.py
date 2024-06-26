from turtle import *
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.num=0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(arg=(f"Score: {self.num}"), align="center",font=('Arial', 13, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center",font=('Arial', 20, 'normal'))
        
    def increase_score(self):
        self.num+=1
        self.clear()
        self.update()