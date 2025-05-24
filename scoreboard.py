from turtle import Turtle
FONT=("Courier",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.score=0
        self.write(f"Level: {self.score}",align="left",font=("Arial",24,"normal"))
    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=("Arial", 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center", font=("Arial", 24, "normal"))


