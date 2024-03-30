def find_word_position(text, word):
    text_lower = text.lower()
    word_lower = word.lower()

    if word_lower in text_lower:
        position = text_lower.find(word_lower) + 1
        print(f"Слово '{word}' найдено в тексте. Позиция: {position}")
    else:
        print(f"Слово '{word}' не найдено в тексте.")

# Получаем ввод от пользователя
text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

# Вызываем функцию для поиска слова
find_word_position(text, word)