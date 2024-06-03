import random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from reward import Reward
import pygame

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Avi 😉")
screen.tracer(False)

all_balls = []
turtle_color = ["red", "yellow", "green"]
x_positions = [-340, -230, -120, -10, 100, 210, 320, 430]
y_positions = [160, 130, 100, 70, 40, 10]

all_tiles = []
# tim = Turtle()
# tim.goto(0, -280)
# tim.left(90)
# tim.color("white")
# tim.hideturtle()
# tim.pensize(width=2)
# for _ in range(28):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
second = 0

def seconds(second):
    screen.tracer(True)
    second += 1
    # timer_tur.clear()
    # timer_tur.write(f"Timer: {second}", font=("Comic Sans MS", 24, "normal"))
    return second


locate = [random.randint(0, 33) for item in range(4)]
new_tim = Turtle()

color = 0
for index in range(len(y_positions)-1):
    for mindex in range(len(x_positions)-1):
        if color == 3:
            color = 0
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.shapesize(stretch_len=5, stretch_wid=1, outline=8)

        tim.color(turtle_color[color])
        if x_positions[mindex] == 320 and index%2 ==0:
            color += 1


        tim.goto(x=x_positions[mindex], y=y_positions[index])
        all_tiles.append(tim)



r_paddle = Paddle(0, -250, "Right", "Left")

pong_ball = Ball()
screen.update()

lives = 3
lives_tur = Turtle()
lives_tur.hideturtle()
lives_tur.penup()
lives_tur.goto(250, 250)
lives_tur.color("white")
lives_tur.pendown()

lives_tur.write(f"Lives: {lives}", font=("Comic Sans MS", 24, "normal"))

hit1 = 0
hit2 = 0
hit3 = 0

timer_tur = Turtle()
timer_tur.hideturtle()
timer_tur.penup()
timer_tur.goto(-50, 250)
timer_tur.color("white")
timer_tur.pendown()
# timer_tur.write(f"Timer: {second}", font=("Comic Sans MS", 24, "normal"))

high_score = Turtle()
high_score.hideturtle()
high_score.penup()
high_score.goto(-380, 250)
high_score.color("white")
high_score.pendown()
with open("score.txt", "r+") as file:
    my_score = file.read()
    high_score.write(f"High Score: {my_score}", font=("Comic Sans MS", 24, "normal"))

counts = 1
game_is_on = True
while game_is_on:
    screen.update()

    # Timer
    seconds(second)
    second += 1


    # Detect Game Over!!
    if counts == 4:

        new_tim.hideturtle()
        new_tim.penup()
        new_tim.goto(-80, 0)
        new_tim.pendown()
        new_tim.color("white")
        new_tim.write("Game Over", font=('Comic Sans MS', 24, 'normal'))
        timer_tur.write(f"Score: {second}", font=("Comic Sans MS", 24, "normal"))
        with open("score.txt", "r+") as file:
            my_score = file.read()
            if second > int(my_score):
                file.write(str(second))
        game_is_on = False

    pong_ball.move()

    # Detect Win
    if not all_tiles:
        screen.tracer(False)
        new_tim.color("white")
        new_tim.goto(-80, 0)
        new_tim.write("You Won", font=("Comic Sans MS", 24, "normal"))
        timer_tur.write(f"Score: {second}", font=("Comic Sans MS", 24, "normal"))
        with open("score.txt", "r+") as file:
            my_score = file.read()
            if second > int(my_score):
                file.write(str(second))
        game_is_on = False

    # Detect collision with the wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    if pong_ball.xcor() > 380 or pong_ball.xcor() < -380:
        pong_ball.bounce_x()
        pong_ball.plus += 0.1


    # Detect collision with the paddle
    if pong_ball.distance(r_paddle) < 50:
        pong_ball.bounce_y()
        pong_ball.plus += 0.1





    # Detect collision with tiles
    for tile in all_tiles:
        if pong_ball.distance(tile) < 50:
            if tile.color()[0] == "red":
                hit1 += 1
            if tile.color()[0] == "yellow":
                hit2 += 1
            if tile.color()[0] == "green":
                hit3 += 1



            if tile.color()[0] == "red" and hit1 == 3:
                all_tiles.remove(tile)
                tile.color("")
                hit1 = 0
            if tile.color()[0] == "yellow" and hit2 == 2:
                all_tiles.remove(tile)
                tile.color("")
                hit2 = 0
            if tile.color()[0] == "green" and hit3 == 1:
                all_tiles.remove(tile)
                tile.color("")
                hit3 = 0

            pong_ball.bounce_y()

            screen.update()

    # Power-ups
    # for rand in locate:
    #     print(rand)
    #     if pong_ball.distance(all_tiles[rand]) < 50:
    #         x_pos = all_tiles[rand].xcor()
    #         print(x_pos)
    #         y_pos = all_tiles[rand].ycor()
    #         print(y_pos)
    #         new_one = Reward(x_pos, y_pos)
    #         all_balls.append(new_one)
    #         new_one.move()
    #         if new_one.distance(r_paddle) < 50:
    #             r_paddle.enlarge()
    #             new_one.color("")
    #
    #     else:
    #         pass
    # for item in locate:
    #     if pong_ball.distance(all_tiles[item]) < 50:



    # Detect the ball goes out of bonds
    if pong_ball.ycor() < -280:
        screen.tracer(False)
        pong_ball.reset_position()
        counts += 1
        lives -= 1
        lives_tur.clear()  # Clear previous text
        lives_tur.write(f"Lives: {lives}", font=("Comic Sans MS", 24, "normal"))



screen.exitonclick()
