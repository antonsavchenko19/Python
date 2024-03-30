import turtle

# Создаем экземпляр черепашки
t = turtle.Turtle()

# Функция для рисования фигуры с заданным количеством углов и цветом
def draw_shape(num_sides, color):
    t.color(color)
    if num_sides == 3:
        for _ in range(num_sides):
            t.forward(50)
            t.right(120)
    elif num_sides == 4:
        for _ in range(num_sides):
            t.forward(50)
            t.right(90)
    elif num_sides == 5:
        for _ in range(num_sides):
            t.forward(50)
            t.right(360 / num_sides)
    else:
        print("Черепашка не может нарисовать фигуру с таким количеством углов")

# Ввод пользователем количества углов и цвета
num_sides = int(input("Введите количество углов (3 - треугольник, 4 - квадрат, 5 - пятиугольник): "))
color = input("Введите цвет (например, 'red', 'blue', 'green'): ")

# Проверка на корректность количества углов и отрисовка фигуры
if num_sides in [3, 4, 5]:
    draw_shape(num_sides, color)
else:
  print("Ошибка! Черепашка не может нарисовать фигуру с таким количеством углов")

# Завершение работы
turtle.done()