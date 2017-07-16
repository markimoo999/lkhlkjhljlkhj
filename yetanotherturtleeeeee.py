import turtle
import time
t = turtle.Pen()
colors = ["red", "green", "blue", "yellow", "pink", "purple", "white", "orange"]
turtle.bgcolor("black")
def polygon(sides, degree, length):
    for x in range(0, sides):
        t.pencolor(colors[x % 8])
        t.forward(length)
        t.right(degree)
while True == True:
    t.penup()
    t.goto(0, 100)
    t.pendown()
    shape = raw_input("enter a shape that i can make with turtle. if you say no, you can X out of the program.\n")
    if shape == "no" or shape == "No":
        break
    else:
        if shape == "triangle" or shape == "square" or shape == "pentagon" or shape == "circle" or shape == "hexagon" or shape == "heptagon" or shape == "octagon" or shape == "enneagon" or shape == "decagon" or shape == "hendecagon" or shape == "dodecagon" or shape == "triskaidecagon":
            diction = {"triangle": [3, 120, 100], "square": [4, 90, 90],"pentagon": [5, 72, 100], "circle": [100, 50, 30], "hexagon": [6, 60, 100], "heptagon": [7, 51.5, 100], "octagon": [8, 45, 100], "enneagon": [9, 39.99, 100], "decagon": [10, 36, 90], "hendecagon": [11, 32.5, 90], "dodecagon": [12, 29.9, 90], "triskaidecagon": [13, 27.5, 80]}
            t.clear()
            ar = diction[shape]
            polygon(ar[0], ar[1], ar[2])
        else:
            print "that's not a shape. go back to school BOIIIIII."

turtle.exitonclick()


