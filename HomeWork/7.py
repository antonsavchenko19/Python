rows = 6

for i in range(1, rows+1):
    # Выводим пробелы перед звёздочками
    for j in range(1, rows-i+1):
        print(" ", end="")
    
    # Выводим звёздочки
    for k in range(1, i*2):
        print("*", end="")
    
    print()