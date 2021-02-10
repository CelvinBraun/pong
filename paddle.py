from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(x=self.x_pos, y=0)


    def paddle_up(self):
        y_cor = self.ycor()+20
        if y_cor < 300:
            self.goto(self.x_pos, y_cor)

    def paddle_down(self):
        y_cor = self.ycor()-20
        if y_cor > -300:
            self.goto(self.x_pos, y_cor)