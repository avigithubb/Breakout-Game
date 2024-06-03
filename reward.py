from turtle import Turtle, Screen

class Reward(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.plus = 1
        self.shape("circle")
        self.color("white")
        self.speed(self.plus)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)
        self.new_y = 10

    def move(self):
        new_y = self.ycor() - self.new_y
        Screen().tracer(True)
        self.goto(self.xcor(), new_y)
