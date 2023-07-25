from turtle import Turtle

# Format Score text
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0                                   # To start counting from zero
        with open("data.txt") as data:
            self.high_score = int(data.read())           # To initialize the high score and save it in data.txt
        self.penup()                                     # To prevent the turtle from writing when it moves to the top
        self.color("white")                              # To make the text white
        self.goto(0, 270)                                # To align the score in the center of the X and at the top of the Y
        self.hideturtle()                                # To make a little arrow disappear
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # To write the score, aligned to the center, and with the font style
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # The reset function is used to change the high_score if there is a new record, save it in Data.txt, and reset the game
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score                  # If the score is a record, it becomes the high_score
            with open("data.txt", mode="w") as data:      # The high_score is overwritten in Data.txt
                data.write(f"{self.high_score}")          # The high_score is converted to a string to be able to write it
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
