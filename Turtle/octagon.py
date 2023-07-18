import turtle

t=turtle.Turtle()

t.pencolor("orange")
t.fillcolor("blue")
t.begin_fill()

for i in range(8):
    t.forward(100)
    t.left(45)
t.end_fill()
