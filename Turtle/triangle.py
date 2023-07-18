import turtle

t=turtle.Turtle()

t.pencolor("brown")
t.fillcolor("yellow")
t.begin_fill()

for i in range(3):
    t.forward(200)
    t.right(120)
t.end_fill()
