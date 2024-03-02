questions = [
    {
        'question': 'Какое имя Булкагова?',
        'options': ['Михаил', 'Аркадий', 'Василий', 'Владислав'],
        'answer': 'Михаил'
    },
    {
        'question': 'Когда было опубликовано стихотворение "Бородино"?',
        'options': ['1845', '1834', '1829', '1837'],
        'answer': '1837'
    },
    {
        'question': 'Какой сегодня год?',
        'options': ['2021', '1812', '2003', '2024'],
        'answer': '2024'
    },
    {
        'question': 'Какой оператор в Python используется для объединения двух списков?',
        'options': ['+', '-', '*', '/'],
        'answer': '+'
    },
    {
        'question': 'Что будет выведено на экран при выполнении следующего кода: print(10 % 3)?',
        'options': ['3', '1', '0', '10'],
        'answer': '1'
    }
]

score = 0

for question in questions:
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input('Введите номер вашего ответа: ')
    if user_answer == str(question['options'].index(question['answer']) + 1):
        print('Правильный ответ!\n')
        score += 1
    else:
        print('Неправильный ответ!\n')

print('Игра окончена!')
print(f'Вы набрали {score}/{len(questions)} очков.')