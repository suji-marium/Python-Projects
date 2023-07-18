import turtle

t=turtle.Turtle()

t.pencolor("red")
t.fillcolor("blue")
t.begin_fill()

for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)

t.end_fill()
