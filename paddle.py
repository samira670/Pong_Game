from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto((x, y))

    def up(self):

        self.goto(self.xcor(), self.ycor()+20)



    def down(self):

        self.goto(self.xcor(), self.ycor()-20)

    def lose(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("game is over")

