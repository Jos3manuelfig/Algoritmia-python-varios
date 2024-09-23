import turtle

def draw_triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)

turtle.speed(1)
draw_triangle()
turtle.done()
