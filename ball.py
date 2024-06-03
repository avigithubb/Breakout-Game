from turtle import Turtle, Screen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.plus = 1
        self.shape("circle")
        self.color("white")
        self.speed(self.plus)

        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, -230)
        self.new_y = 10
        self.new_x = 10

    def move(self):
        new_x = self.xcor() + self.new_x
        new_y = self.ycor() + self.new_y
        Screen().tracer(True)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.new_y *= -1

    def bounce_x(self):
        self.new_x *= -1
        self.speed(self.plus + 1)
        speedometer = self.speed()
        print(speedometer)

    def reset_position(self):
        self.goto(0, -240)
        self.plus = 1
        self.bounce_x()
