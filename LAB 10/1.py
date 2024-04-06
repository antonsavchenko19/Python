rightCounter = 0
questionsCounter = 0

questions = [
    "Сколько цветов у радуги?",
    "Какой язык мы изучаем?",
    "Сколько планет в Солнечной системе?",
    "Как называется столица Франции?",
    "Что такое HTML?"
]

rightAnswers = [
    "7",
    "python",
    "8",
    "Париж",
    "Язык разметки гипертекста"
]

while questionsCounter < len(questions):
    answer = input(questions[questionsCounter])
    if answer.lower() == rightAnswers[questionsCounter].lower():
        rightCounter += 1
        print("Вы ответили верно!")
    else:
        print("Вы ответили неверно.")
    questionsCounter += 1

print(f"Вы набрали баллов: {rightCounter}")