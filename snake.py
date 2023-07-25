from turtle import Turtle

# "To make three squares of 20x20 appear, one after the other, with starting positions and a for loop
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Constants are created to prevent the snake from changing its head and reversing its position
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]         # It says that the head will be the first segment

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)       # It's a for loop to add segments

    def add_segment(self, position):
        new_segment = Turtle("square")       # So that each turtle has a square shape
        new_segment.color("white")           # So that each square is white in color
        new_segment.penup()                  # So that the outline of each square is not drawn as it moves
        new_segment.goto(position)           # So that all the squares start at the position of 'starting
        self.segments.append(new_segment)    # To add each created segment to the 'segments' list.

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)              # A for loop to move the snake that lost far away from the screen
        self.segments.clear()                # To clear the snake that lost
        self.create_snake()                  # To create a new snake
        self.head = self.segments[0]         # So that the new snake is the same as the previous one

    def extend(self):
        self.add_segment(self.segments[-1].position())  # To make the added segment go to the last position

    def move(self):
        # The idea of this function is that the posterior segment always takes the place of the segment that comes before it
        # To make the last segment take the position of the penultimate segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # The functions to listen for keyboard events
    def up(self):
        if self.head.heading() != DOWN:     # To prevent the head and the entire direction from changing
            self.head.setheading(UP)        # A change of direction is applied to the first segment

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
