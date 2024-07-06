import turtle
import numpy as np

# Define the unit of measurement for the shapes
UNIT = 40

def square_shape(principal_direction):
    """
    Function to draw a square shape with the turtle graphics.
    The square is drawn based on the principal direction provided.

    Args:
    principal_direction (int): The principal direction in which the square is to be drawn.
    """
    tr.pendown()
    tr.setheading(principal_direction)
    tr.right(45)
    tr.begin_fill()

    for _ in range(4):
        tr.forward(UNIT)
        tr.left(90)

    tr.end_fill()
    tr.penup()
    tr.setheading(principal_direction)
    tr.forward(np.sqrt(2) * UNIT)


def draw_arrow_wing(scale, hand):
    """
    Function to draw a wing of an arrow shape with the turtle graphics.
    The wing is drawn based on the scale and hand provided.

    Args:
    scale (int): The scale of the wing.
    hand (int): The hand of the wing. 1 for right wing and -1 for left wing.
    """
    tr.pendown()
    tr.right(hand * 135)
    tr.forward(2 * scale * UNIT)
    tr.left(hand * 90)
    tr.forward(UNIT)
    tr.left(hand * 90)
    tr.forward((2 * scale + 1) * UNIT)
    tr.penup()


def arrow_shape(principal_direction, scale):
    """
    Function to draw an arrow shape with the turtle graphics.
    The arrow is drawn based on the principal direction and scale provided.

    Args:
    principal_direction (int): The principal direction in which the arrow is to be drawn.
    scale (int): The scale of the arrow.
    """
    tr.setheading(principal_direction)
    tr.forward(np.sqrt(2) * UNIT)
    arrow_origin = tr.pos()
    tr.begin_fill()

    draw_arrow_wing(scale, 1)  # right wing

    tr.goto(arrow_origin[0], arrow_origin[1])  # return to the arrow origin
    tr.setheading(principal_direction)

    draw_arrow_wing(scale, -1)  # left wing

    tr.end_fill()
    tr.penup()


def move_to_next(next_direction):
    """
    Function to move the turtle to the next position.

    Args:
    next_direction (int): The direction in which the turtle is to be moved.
    """
    tr.penup()
    tr.setheading(next_direction)
    tr.right(45)
    tr.forward(UNIT)


def goto_start():
    """
    Function to move the turtle to the start position.
    """
    tr.penup()
    tr.setheading(180)
    tr.forward(0.5 * np.sqrt(2) * UNIT)

    tr.left(45)
    tr.forward(7 * UNIT)


# Set up the turtle
tr = turtle.Turtle()
tr.screen.bgcolor('#eeeeee')
tr.shape('turtle')
tr.screen.title('Oranim')
tr.speed(0)
tr.color('#074c45')

goto_start()

# Draw the shapes
for direction in [90, 0, -90]:
    square_shape(direction)
    arrow_shape(direction, 1)
    arrow_shape(direction, 2)
    arrow_shape(direction, 3)
    move_to_next(direction)

tr.home()

# Exit on click
turtle.Screen().exitonclick()