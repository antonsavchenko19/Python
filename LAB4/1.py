age = int(input("Введите возраст: "))

if age > 0 and age <= 10:
    print("Вы ребёнок")
elif age > 10 and age <= 16:
    print("Вы подросток")
elif age > 16 and age <= 22:
    print("Вы молодой человек (18-22)")
elif age > 22 and age <= 30:
    print("Вы молодой человек (23-30)")
elif age > 30 and age < 50:
    print("Вы взрослый")
elif age >= 50 and age < 120:
    print("Вы пожилой человек")
else:
    print("Возраст введён неверно!")