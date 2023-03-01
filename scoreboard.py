from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 275)
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def score_point(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.display_score()
