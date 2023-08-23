from turtle import Screen

import Snake
from Snake import snake,Food
from scoreboard import Scoreboard,collsion
import time
screen=Screen()
screen.bgcolor("black")
screen.title("Snake Game ")
screen.setup(600,600)
s=snake()
s.create_snake()
f=Food()
screen.tracer(0)
f.food()
screen.listen()
screen.onkey(s.up,"w")
screen.onkey(s.down,"s")
screen.onkey(s.right,"d")
screen.onkey(s.left,"a")
scoe=Scoreboard()
game_on=True
g=collsion()
while game_on:
    time.sleep(0.1)
    screen.update()
    scoe.score()
    s.sanke_move()
    if (s.snake_name[0].distance(f.a.xcor(),f.a.ycor())<15):
        f.food()
        s.extend()
        scoe.s+=1
        scoe.rem()
        scoe.score()
    if(s.snake_name[0].xcor()>300 or s.snake_name[0].xcor()<-300):
        g.colloide()
        game_on=False
    elif(s.snake_name[0].ycor()>300 or s.snake_name[0].ycor()<-300):
        g.colloide()
        game_on=False
    v=[]
    for i in range(1,len(s.snake_name)-1):
        v.append(s.snake_name[i])
    for i in v:
        if(s.snake_name[0].distance(i)<10):
            g.colloide()
            game_on=False


screen.exitonclick()