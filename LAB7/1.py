import random
guess = int(input("Введите ваше число: "))
target = 100

difference = guess - target

if difference <= 2 and difference >= -2:

    print("Горячо!")

elif difference <= 4 and difference >= 3:

    print("Тепло!")

else:

    print("Холодно!")