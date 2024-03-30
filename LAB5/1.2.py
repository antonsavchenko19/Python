import turtle

# Создаем экземпляр черепашки
t = turtle.Turtle()

# Функция для рисования фигуры с заданным количеством углов и цветом
def draw_shape(num_sides, color):
    t.color(color)
    for _ in range(num_sides):
        t.forward(50)
        t.right(360 / num_sides)

# Ввод пользователем количества углов и цвета
num_sides = int(input("Введите количество углов (3 - треугольник, 4 - квадрат, 5 - пятиугольник): "))
color = input("Введите цвет (например, 'red', 'blue', 'green'): ")

# Проверка на корректность количества углов и отрисовка фигуры
if num_sides == 3:
    draw_shape(3, color)
elif num_sides == 4:
    draw_shape(4, color)
elif num_sides == 5:
    draw_shape(5, color)
else:
    print("Черепашка не может нарисовать фигуру с таким количеством углов")

# Завершение работы
turtle.done()