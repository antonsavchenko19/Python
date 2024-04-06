import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Нижняя часть снеговика
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# Средняя часть снеговика
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(70)

# Голова снеговика
t.penup()
t.goto(0, 100)
t.pendown()
t.circle(40)

turtle.done()