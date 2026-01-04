from turtle import Turtle


MOVE_DISTANCE = 20



class Paddle(Turtle):
    def __init__(self, x_pos,y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.pu()
        self.goto(x_pos,y_pos)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)



