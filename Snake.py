from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.a=Turtle("circle")
    def food(self):
        post=[]
        for i in range(0,270,20):
            post.append(i)
        self.a.penup()
        self.a.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.a.color("red")
        self.a.goto(random.choice(post),random.choice(post))

class snake(Food):
    def __init__(self):
        super().__init__()
        self.snake_name=[]
        self.pos = [(0, 0), (-20, 0), (-40, 0)]
    def create_snake(self):
        for i in self.pos:
            nikunj=Turtle("square")
            nikunj.color("white")
            nikunj.penup()
            nikunj.goto(i)
            nikunj.speed("fast")
            self.snake_name.append(nikunj)
    def sanke_move(self):
            for snake_numer in range(len(self.snake_name)-1,0,-1):
                xx=self.snake_name[snake_numer-1].xcor()
                yy=self.snake_name[snake_numer-1].ycor()
                self.snake_name[snake_numer].goto(x=xx,y=yy)
            self.snake_name[0].forward(20)
    def extend(self):
        newtur=Turtle()
        newtur.color("white")
        newtur.penup()
        newtur.shape("square")
        newtur.goto(self.snake_name[-1].xcor(),self.snake_name[-1].ycor())
        temp=(newtur.xcor(),newtur.ycor())
        self.pos.append(temp)
        self.snake_name.append(newtur)


    def up(self):
        self.snake_name[0].setheading(90)
    def down(self):
        self.snake_name[0].setheading(270)
    def right(self):
        self.snake_name[0].setheading(0)
    def left(self):
        self.snake_name[0].setheading(180)