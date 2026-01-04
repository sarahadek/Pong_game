from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time



screen = Screen()
ball = Ball()
scoreboard = Scoreboard()




right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)




screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG")
screen.tracer(0)


screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# left paddle movement

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detect wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        # bounce
        ball.bounce_y()
        #detect collision in the right paddle
    if ball.distance(right_paddle) <50 and ball.xcor() > 320 or ball.distance(left_paddle) <50 and ball.xcor()< -320:
        ball.bounce_x()
    # detect when the ball misses on the right
    if ball.xcor()>380:
        ball.reset()
        scoreboard.left_point()
    # detect when ball misses on the left
    if ball.xcor()< -380:
        ball.reset()
        scoreboard.right_point()

    if scoreboard.right_score == 2 or scoreboard.left_score == 2:
        game_on = False
        print ("GAME OVER")



screen.exitonclick()


