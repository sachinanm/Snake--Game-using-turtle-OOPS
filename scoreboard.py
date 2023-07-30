from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"SCORE: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()  # to clear previous score so that it don't overlap
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGN, font=FONT)