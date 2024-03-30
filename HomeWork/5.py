import turtle

# Настройка черепашки
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("black")
pen.speed(5)

# Рисование квадрата (дом)
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.right(90)
pen.end_fill()

# Рисование треугольной крыши
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.begin_fill()
pen.goto(0, 200)
pen.goto(100, 100)
pen.goto(-100, 100)
pen.end_fill()

# Рисование двери
pen.penup()
pen.goto(-30, -100)
pen.pendown()
pen.color("brown")
pen.begin_fill()
pen.goto(30, -100)
pen.goto(30, 0)
pen.goto(-30, 0)
pen.goto(-30, -100)
pen.end_fill()

# Рисование окон
pen.penup()
pen.goto(-80, -30)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.goto(-40, -30)
pen.goto(-40, 10)
pen.goto(-80, 10)
pen.goto(-80, -30)
pen.end_fill()

pen.penup()
pen.goto(40, -30)
pen.pendown()
pen.begin_fill()
pen.goto(80, -30)
pen.goto(80, 10)
pen.goto(40, 10)
pen.goto(40, -30)
pen.end_fill()

# Завершение программы
turtle.done()