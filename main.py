from score import Score
from paddle import Paddle
from ball import Ball
from turtle import Screen
import time

# screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

l_pedal = Paddle(-350)
r_pedal = Paddle(350)
ball = Ball()
score = Score()

game_is_on = True

while game_is_on:
    screen.listen()
    screen.onkey(key="w", fun=l_pedal.paddle_up)
    screen.onkey(key="s", fun=l_pedal.paddle_down)
    screen.onkey(key="Up", fun=r_pedal.paddle_up)
    screen.onkey(key="Down", fun=r_pedal.paddle_down)

    ball.move()

    time.sleep(0.1)
    screen.update()

    # wall collision
    if ball.ycor()>220 or ball.ycor()<-300:
        ball.bounce()

    # paddle collision right paddle
    if ball.xcor()>320 and ball.distance(r_pedal)<50 or ball.xcor()<-320 and ball.distance(l_pedal)<50:
        ball.paddle_bounce()

    if ball.xcor()>350:
        score.p1_score+=1
        score.update_score()
        time.sleep(1)
        ball.reset()
        ball = Ball()
        ball.x_move *= -1

    if ball.xcor()<-350:
        score.p2_score+=1
        score.update_score()
        time.sleep(1)
        ball.reset()
        ball.x_move *= -1
        ball = Ball()

screen.exitonclick()