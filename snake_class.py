from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []  # How long the snake is
        self.create_snake()  # Calls the function to create the initial snake
        self.head = self.body[0]  # The head of the snake
        self.positions = []  # The positions of all parts of the snake

    def create_snake(self):
        """Creates the initial 3 bodied snake"""
        for body in range(3):
            new_body = Turtle("square")
            new_body.color("white")
            new_body.penup()
            new_x, new_y = body * -20, 0
            new_body.goto(new_x, new_y)
            self.body.append(new_body)

    def add_body(self):
        """add a new body and appends it to the self.body"""
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        self.body.append(new_body)

    def move(self):
        """Moves the snake head, and the body"""
        for index in range(len(self.body) - 1, 0, -1):
            new_x = self.body[index - 1].xcor()
            new_y = self.body[index - 1].ycor()
            self.body[index].goto(new_x, new_y)  # Go to the position of the next body
        self.head.forward(20)  # Forward head

    def move_up(self):
        """Moves the snake head NORTH"""
        print("UP")
        if self.head.heading() != 270:  # Move UP only if not facing DOWN
            self.body[0].setheading(90)
        else:
            print("UP turn Failed")

    def move_down(self):
        """Moves the snake head SOUTH"""
        print("DOWN")
        if self.head.heading() != 90:  # Go DOWN only if not facing UP
            self.body[0].setheading(270)
        else:
            print("DOWN turn Failed")

    def move_left(self):
        """Moves the snake head WEST"""
        print("LEFT")
        if self.head.heading() != 0:  # Move LEFT only if not facing RIGHT
            self.body[0].setheading(180)
        else:
            print("LEFT turn Failed")

    def move_right(self):
        """Moves the snake head EAST"""
        print("RIGHT")
        if self.head.heading() != 180:  # Move RIGHT only if not facing LEFT
            self.body[0].setheading(0)
        else:
            print("RIGHT turn Failed")

    def update_position(self):
        """Puts all the positions of all the body of the snake"""
        self.positions.clear()
        for body in range(1, len(self.body)):  # append all body positions in self.positions
            self.positions.append(self.body[body].position())
        print(self.positions)

    def collision(self):
        """Check if snake head collides with wall or its body"""
        # Check collision with wall
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            print("COLLISION WITH WALL")
            return True

        for pos in self.positions:  # Check collision with TAIL
            if self.head.distance(pos) < 15:
                print("COLLISION WITH TAIL !!!!")
                # turtle.bye()
                return True

        return False
