from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        self.penup()
        self.x = 10
        self.y = 10




    def move(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)



    def bounce(self):
            self.y = -1 * self.y

    def bouncex(self):
        self.x = -1* self.x

    def lose(self):
        self.hideturtle()
        self.goto(-100, 0)
        self.color("red")
        self.write("Game is Over", font=("Arial", 30, "normal"))
