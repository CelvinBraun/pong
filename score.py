from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.p1_score = 0
        self.p2_score = 0
        self.goto(-70, 220)
        self.write(self.p1_score, align="center", font=("Courier", 60 , "normal"))
        self.goto(0, 240)
        self.write("vs.", align="center", font=("Courier", 30, "normal"))
        self.goto(70, 220)
        self.write(self.p2_score, align="center", font=("Courier", 60, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-70, 220)
        self.write(self.p1_score, align="center", font=("Courier", 60, "normal"))
        self.goto(0, 240)
        self.write("vs.", align="center", font=("Courier", 30, "normal"))
        self.goto(70, 220)
        self.write(self.p2_score, align="center", font=("Courier", 60, "normal"))