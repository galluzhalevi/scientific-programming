import turtle


START_POSITIONS = [(-110, -25),
                   (0, -25),
                   (110, -25),
                   (-55, -75),
                   (55, -75)]

DEFAULT_COLORS = ['blue', 'red', 'green', 'yellow', 'black']


def draw_circle(tr, color, start_position, radius=45):
    tr.penup()
    tr.goto(start_position)
    tr.pendown()
    tr.color(color)
    tr.circle(radius)


def get_colors(count):
    colors_list = list()
    print(f'Please enter {count} colors')
    for i in range(count):
        next_color = input("Enter the next color: ")
        if next_color == '':
            next_color = DEFAULT_COLORS[i]
        colors_list.append(next_color)
    return colors_list


def main():
    colors_list = get_colors(len(START_POSITIONS))
    tr = turtle.Turtle()
    tr.speed(7)
    tr.shape('turtle')
    tr.pensize(5)

    for i in range(len(START_POSITIONS)):
        draw_circle(tr, colors_list[i], START_POSITIONS[i])

    turtle.Screen().exitonclick()


main()


# Please enter 5 colors
# Enter the next color: blue
# Enter the next color: green
# Enter the next color: black
# Enter the next color: yellow
# Enter the next color: red