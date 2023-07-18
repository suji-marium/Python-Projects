import turtle

t=turtle.Turtle()

t.pencolor("green")
t.fillcolor("red")
t.begin_fill()

for i in range(6):
    t.forward(100)
    t.left(60)
t.end_fill()
