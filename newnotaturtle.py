import turtle
t = turtle.Pen()
colors = ["red", "green", "blue"]
def polygon(sides, degree, length, othlen, deg2):
    for x in range(0, sides):
        t.pencolor(colors[x%3])
        t.forward(length)
        t.right(degree)
        t.backward(othlen)
        t.left(deg2)
polygon(200, 30, 35, 90, 95)
turtle.exitonclick()