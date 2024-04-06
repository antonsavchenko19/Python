import random

print("Добро пожаловать в игру 'Камень, ножницы, бумага, ящерица, Спок'!")
playerScore = 0
botScore = 0
rounds_played = 0
valid_choices = ["камень", "ножницы", "бумага", "ящерица", "спок"]

while rounds_played < 5:
    rounds_played += 1
    
    print(f"\nРаунд {rounds_played}")
    answer = input("Что выберешь? (Введите номер варианта)\n1. Камень\n2. Ножницы\n3. Бумага\n4. Ящерица\n5. Спок\n")
    answer = valid_choices[int(answer) - 1]

    if answer in valid_choices:
        botAnswer = random.choice(valid_choices)
        print(f"А я выберу {botAnswer}")
        
        if answer == botAnswer:
            print("Ничья!")
        elif (answer == "камень" and (botAnswer == "ножницы" or botAnswer == "ящерица")) or \
             (answer == "ножницы" and (botAnswer == "бумага" or botAnswer == "ящерица")) or \
             (answer == "бумага" and (botAnswer == "камень" or botAnswer == "Спок")) or \
             (answer == "ящерица" and (botAnswer == "бумага" or botAnswer == "Спок")) or \
             (answer == "спок" and (botAnswer == "камень" or botAnswer == "ножницы")):
            print("Ты победил!")
            playerScore += 1
        else:
            print("Я победил!")
            botScore += 1
    else:
        print("Выбери из предложенных вариантов!")
        
if playerScore == botScore:
    print("Ничья по итогам пяти раундов!")
elif playerScore > botScore:
    print("Ты победил по итогам пяти раундов")
else:
    print("Я победил по итогам пяти раундов")