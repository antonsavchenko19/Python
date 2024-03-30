import turtle
# Создаем экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()
# Концы звезды 
kolvo = 9
for _ in range(kolvo):
    t.forward(100) 
    # Длина 
    t.right(360 / kolvo * 2)  
    # Угол поворота 
# Конец
screen.mainloop()