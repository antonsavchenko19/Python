studentList = ["Вася", "Петя", "Никита", "Владислав", "Виктория", "Марина"]

while True:
    answer = int(input("Выберите действие\n"
                       "1 - добавить студента\n"
                       "2 - удалить студента\n"
                       "3 - посмотреть весь список студентов\n"
                       "0 - выйти из программы\n"))
    if answer not in [1, 2, 3, 0]:
        print("Такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("Введите имя студента: ")
        studentList.append(newStudent)
    elif answer == 2:
        delStudent = input("Введите имя студента для удаления: ")
        if delStudent in studentList:
            studentList.remove(delStudent)
        else:
            print("Такого студента нет в списке")
    elif answer == 3:
        print(studentList)
    elif answer == 0:
        break