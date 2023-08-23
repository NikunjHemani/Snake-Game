from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.d=Turtle()
        self.s=0

    def score(self):
        self.d.penup()
        self.d.color("white")
        self.d.hideturtle()
        self.d.goto(x=0,y=270)
        self.d.write(f"Score : {self.s}",align="center",font=('Arial', 15, 'normal'))
    def rem(self):
        self.d.clear()

class collsion(Turtle):
    def __init__(self):
        super().__init__()
    def colloide(self):
        a=Turtle()
        a.color("white")
        a.penup()
        a.hideturtle()
        a.goto(0,0)
        a.write("Game Over",align="center",font=('Arial', 30, 'normal'))
