from turtle import Turtle

SCORE_BOARD_POSITION = (0, 270)
SCORE_BOARD_FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=SCORE_BOARD_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=SCORE_BOARD_FONT)

