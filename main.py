import os
from teacher import Teacher
from studentGroup import StudentGroup
from globalSegment import dateTimeValidate, clear, strHasOnlyLetters, studentsWorkDaysTime

# functions
def mainMenu():
    clear()
    print("1 - ввести список учителей")
    print("2 - ввести список классов")
    print("3 - заполнить время уроков")
    # print("3 - необходимые условия")
    # print("4 - составить расписание (xlsx/txt)")
    print("7 - ТЕСТ ФУНКЦИЯ")
    # print("5 - выход")

def studentsWorkDaysTimeEnter():
    maxCountOfLessons = int(input("Введите максимальное кол-во уроков в смене: "))
    for i in range(1, maxCountOfLessons+1):
        while True:
            subjectTime = str(input(f"Введите длительность {i} урока (форма ввода: XX:XX-XX:XX), если же урока нет, то введите 0: "))
            if dateTimeValidate(subjectTime):
                break
        studentsWorkDaysTime.append(subjectTime)

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
                # studentGroup.fillWorkDays()
                studentGroups.append(studentGroup)
            case 2:
                break


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
                break
            case 7:
                for i in teacherList:
                    print(i.name)
                    print(i.subject)
                    for j in i.workDays.keys():
                        print(f"{j}: {i.workDays[j]}")
                os.system("pause")


if __name__ == "__main__":
    main()