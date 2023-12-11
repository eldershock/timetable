import os
from teacher import Teacher
from studentGroup import StudentGroup
from globalSegment import dateTimeValidate, clear, strHasOnlyLetters, studentsWorkDaysTime, strIsInt


# functions
def mainMenu():
    clear()
    print("1 - ввести список учителей")
    print("2 - ввести список классов")
    print("3 - заполнить время уроков")
    # print("3 - необходимые условия")
    print("4 - составить расписание (xlsx/txt)")
    print("7 - ТЕСТ ФУНКЦИЯ")
    # print("5 - выход")


# def makeTimetable(teacherList: list(), studentGroups: list()):


#teacher's segment
def teachersMenu():
    clear()
    print("1 - ввести учителя")
    print("2 - вернуться назад")


def inputTeacherList(teacherList: list):
    while True:
        teachersMenu()
        menuButton = int(input())
        match(menuButton):
            case 1:
                while True:
                    name = str(input("Введите имя учителя: "))
                    if strHasOnlyLetters(name):
                        break
                while True:
                    subject = str(input("Введите предмет: "))
                    if strHasOnlyLetters(subject):
                        break
                teacher = Teacher(name, subject)
                teacher.fillWorkDays()
                teacherList.append(teacher)
            case 2:
                break


#student's segment
def studentGroupMenu():
    clear()
    print("1 - ввести группу")
    print("2 - вернуться назад")


def inputStudentGroup(studentGroups: list):
    while True:
        studentGroupMenu()
        menuButton = int(input())
        match(menuButton):
            case 1:
                groupName = str(input("Введите название класса: "))
                groupCount = int(input("Введите кол-во учеников: "))
                studentGroup = StudentGroup(groupName, groupCount)
                studentGroup.fillWorkDays(studentsWorkDaysTime)
                studentGroups.append(studentGroup)
            case 2:
                break


def studentsWorkDaysTimeEnter():
    maxCountOfLessons = str(input("Введите максимальное кол-во уроков в смене: "))
    while True:
        if strIsInt(maxCountOfLessons):
            break
        else:
            maxCountOfLessons = str(input())
    for i in range(int(maxCountOfLessons)):
        while True:
            subjectTime = str(input(f"Введите длительность {i+1} урока (форма ввода: XX:XX-XX:XX): "))
            if dateTimeValidate(subjectTime, True):
                break
        studentsWorkDaysTime.append(subjectTime)


def main():
    choice = 0
    teacherList = list()
    studentGroups = list()
    while True:
        mainMenu()
        choice = int(input("Выберите действие: "))
        match (choice):
            case 1:
                inputTeacherList(teacherList)
            case 2:
                inputStudentGroup(studentGroups)
            case 3:
                studentsWorkDaysTimeEnter()
            case 4:
                makeTimetable(teacherList, studentGroups)
                break
            case 5:
                for i in studentGroups:
                    print(i.groupName)
                    print(i.count)
                    for j in i.workDays.keys():
                        print(f"{j}: {i.workDays[j]}")
                print(f"Время уроков: {studentsWorkDaysTime}")
                os.system("pause")
            case 7:
                for i in teacherList:
                    print(i.name)
                    print(i.subject)
                    for j in i.workDays.keys():
                        print(f"{j}: {i.workDays[j]}")
                os.system("pause")


if __name__ == "__main__":
    main()