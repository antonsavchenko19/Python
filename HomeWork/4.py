# Запрос суммы в рублях и валюты, в которую нужно конвертировать
amount = float(input("Введите сумму в рублях: "))
currency = input("Выберите валюту для конвертации (доллары, евро, юани): ")

# Курс валюты (здесь приведены примерные значения, обновите их по необходимости)
usd_rate = 0.014  # 1 USD = 71 RUB (примерное значение на момент написания)
eur_rate = 0.012  # 1 EUR = 83 RUB (примерное значение на момент написания)
cny_rate = 0.091  # 1 CNY = 11 RUB (примерное значение на момент написания)

# Конвертация суммы
if currency.lower() == "доллары":
    converted_amount = amount * usd_rate
    print(f"{amount} рублей составляют примерно {converted_amount:.2f} долларов")
elif currency.lower() == "евро":
    converted_amount = amount * eur_rate
    print(f"{amount} рублей составляют примерно {converted_amount:.2f} евро")
elif currency.lower() == "юани":
    converted_amount = amount * cny_rate
    print(f"{amount} рублей составляют примерно {converted_amount:.2f} юаней")
else:
    print("Такой валюты нет в списке конвертации.")