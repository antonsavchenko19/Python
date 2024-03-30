studentList = ["Вася", "Петя", "Никита", "Владислав", "Виктория", "Марина"]
gradesList = []  # Список для оценок

while True:
    answer = int(input("Выберите действие\n"
                       "1 - добавить студента\n"
                       "2 - удалить студента\n"
                       "3 - посмотреть весь список студентов\n"
                       "4 - добавить оценку студенту\n"
                       "5 - посмотреть весь список оценок\n"
                       "0 - выйти из программы\n"))

    if answer not in [1, 2, 3, 4, 5, 0]:
        print("Такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("Введите имя студента: ")
        studentList.append(newStudent)
        
        newGrade = int(input("Введите оценку для студента: "))
        gradesList.append(newGrade)
    elif answer == 2:
        delStudent = input("Введите имя студента для удаления: ")
        if delStudent in studentList:
            index = studentList.index(delStudent)
            del studentList[index]
            del gradesList[index]
        else:
            print("Такого студента нет в списке")
    elif answer == 3:
        print(studentList)
    elif answer == 4:
        student = input("Введите имя студента, которому добавить оценку: ")
        if student in studentList:
            index = studentList.index(student)
            newGrade = int(input("Введите оценку для студента: "))
            gradesList[index] = newGrade
        else:
            print("Такого студента нет в списке")
    elif answer == 5:
        print(gradesList)
    elif answer == 0:
        break