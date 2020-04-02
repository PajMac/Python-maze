import turtle

t = turtle.Turtle()
t.speed(5)
for i in range(3):
    t.forward(100)
    t.penup()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.pendown()
    t.forward(100)
    t.penup()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.pendown()
    t.forward(1)


clone = t.clone()
clone.color("blue")
#clone.goto(90,100)
clone.forward(20)
turtle.done()

