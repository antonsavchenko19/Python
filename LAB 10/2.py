import random

timeList = ["Сегодня", "Завтра", "Очень скоро"]
eventList = ["вы встретите", "с вами случится", "вы найдёте"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]

while True:
    zodiac_sign = input("Введите знак Зодиака: ").lower()

    if zodiac_sign not in ["овен", "телец", "близнецы", "рак", "лев", "дева", "весы", "скорпион", "стрелец", "козерог", "водолей", "рыбы"]:
        print("Введен некорректный знак Зодиака. Повторите ввод.")
        continue

    time = timeList[random.randint(0, len(timeList) - 1)]
    event = eventList[random.randint(0, len(eventList) - 1)]
    obj = objectList[random.randint(0, len(objectList) - 1)]

    print(time + " " + event + " " + obj)

    next_attempt = input("Хотите попробовать ещё раз? (да/нет): ")
    if next_attempt.lower() != "да":
        break

print("Приходите ещё за новыми предсказаниями!")