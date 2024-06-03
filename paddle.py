from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, x, y, on_key_right, on_key_left):
        super().__init__()
        self.penup()
        self.shape("square")
        self.width = 1
        self.len = 5
        self.shapesize(stretch_len=self.len, stretch_wid=self.width)
        self.color("white")
        self.goto(x=x, y=y)

        Screen().listen()

        Screen().onkey(key=on_key_right, fun=self.move_right)
        Screen().onkey(key=on_key_left, fun=self.move_left)

    def move_right(self):
        new_x = self.ycor() + 20
        self.goto(self.xcor() + 80, -250)

    def move_left(self):
        new_x = self.ycor() - 20
        self.goto(self.xcor() - 80, -250)

    def enlarge(self):
        new_len = self.len + 2
        self.shapesize(stretch_wid=self.width, stretch_len=new_len)
