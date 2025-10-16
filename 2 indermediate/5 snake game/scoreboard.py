from turtle import Turtle
ALINMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALINMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
        
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALINMENT, font=FONT)