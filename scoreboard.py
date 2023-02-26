from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 275)
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def score_point(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)
