import turtle

t=turtle.Turtle()

t.pencolor("red")
t.fillcolor("green")
t.begin_fill()

for i in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()
