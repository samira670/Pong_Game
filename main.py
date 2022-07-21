from turtle import Screen , Turtle
from ball import Ball
import time
from paddle import Paddle
screen = Screen()
screen.tracer(0)
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Welcome to Pong Game")

game_is_on = True

ball= Ball()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if  ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    elif ball.distance(r_paddle.xcor(), r_paddle.ycor())< 50 and ball.xcor()>340:
        ball.bouncex()

    elif ball.distance(l_paddle.xcor(), l_paddle.ycor())< 50 and ball.xcor()<-350:
        ball.bouncex()
    elif ball.xcor()>390 or ball.xcor()>390 :
        print("you lose the game")
        game_is_on = False
        ball.lose()

















screen.exitonclick()
