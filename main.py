import os
import random
from teacher import Teacher
from studentGroup import StudentGroup
from globalSegment import dateTimeValidate, clear, strHasOnlyLetters, studentsWorkDaysTime, strIsInt, workDaysConst


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


def makeTimetable(teacherList: list(), studentGroups: list()):
    timetable = {}
    usedTeachers = []
    usedSubjects = {}
    availableTeachers = []
    for studentGroup in studentGroups:
        groupTimetable = {}
        for day in workDaysConst:
            daySubjects = []
            subject = ""
            teacher = ""
            subjectPerDay = 0
            exit = False
            for time in studentsWorkDaysTime:
                if subject in usedSubjects and usedSubjects[subject] == 0:
                    usedSubjects.pop(subject)
                if subjectPerDay <= 0:
                    while True:
                        if subject not in daySubjects and subject != "":
                            daySubjects.append(subject)
                            print(subject)
                            break
                        if len(daySubjects) == len(list(studentGroup.subjects.keys())):
                            exit = True
                            break
                        subject = random.choice(list(studentGroup.subjects.keys()))
                    if exit:
                        break
                    # subject = random.choice(list(studentGroup.subjects.keys()))
                    usedSubjects[subject] = studentGroup.subjects[subject]
                    hours = studentGroup.subjects[subject]
                    subjectPerDay = int(hours // len(workDaysConst))
                    teacher = ""
                    availableTeachers = [teacher for teacher in teacherList if teacher.subject == subject]
                    
                if not availableTeachers:
                    print(f"Ошибка: Нет доступных учителей для предмета {subject} в группе {studentGroup.groupName}.")
                    return
                
                if teacher == "":
                    teacher = random.choice(availableTeachers)
                    del availableTeachers[availableTeachers.index(teacher)]
                if day not in groupTimetable:
                    groupTimetable[day] = []
                
                groupTimetable[day].append({
                    'subject': subject,
                    'teacher': teacher.name,
                    'time': time
                })

                subjectPerDay -= 1
                usedSubjects[subject] -= 1
        timetable[studentGroup.groupName] = groupTimetable

    # Вывод расписания
    for group, groupTimetable in timetable.items():
        print(f"\nРасписание для группы {group}:\n")
        for day, lessons in groupTimetable.items():
            print(f"{day}:")
            for lesson in lessons:
                print(f"    Предмет: {lesson['subject']}")
                print(f"    Учитель: {lesson['teacher']}")
                print(f"    Время: {lesson['time']}")
                print()
    

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
                studentGroup.fillSubjects()
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
    teacher1 = Teacher("Иванов", "Математика", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher2 = Teacher("Петров", "Физика", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher3 = Teacher("Куренков", "История", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher4 = Teacher("Владимир", "Химия", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher5 = Teacher("Влад", "Геометрия", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher6 = Teacher("Билборды", "залупа", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher7 = Teacher("Бустер", "Матанализ", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher8 = Teacher("Кола", "хуйня", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher9 = Teacher("Вла1д", "Геометрия", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher10 = Teacher("Вл23ад", "Геометрия", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    teacher11 = Teacher("Владим2ир", "Химия", {"Понедельник": ["07:00", "19:00"], "Вторник": ["07:00", "19:00"], "Среда": ["07:00", "19:00"], "Четверг": ["07:00", "19:00"], "Пятница": ["07:00", "19:00"], "Суббота": ["07:00", "19:00"]})
    group1 = StudentGroup("Группа 1", {"Математика": 10, "Физика": 5, "История": 10, "Химия": 15, "Геометрия" : 16, "Матанализ" : 10}, 14)
    group2 = StudentGroup("Группа 2", {"Математика": 7, "Физика": 5, "История": 10, "хуйня": 10, "залупа" : 4}, 15)
    choice = 0
    teacherList = list()
    teacherList.append(teacher1)
    teacherList.append(teacher2)
    teacherList.append(teacher3)
    teacherList.append(teacher4)
    teacherList.append(teacher5)
    teacherList.append(teacher6)
    teacherList.append(teacher7)
    teacherList.append(teacher8)
    teacherList.append(teacher9)
    teacherList.append(teacher10)
    teacherList.append(teacher11)
    studentGroups = list()
    studentGroups.append(group1)
    studentGroups.append(group2)
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
                for studentGroup in studentGroups:
                    print("Класс: ", studentGroup.groupName, "кол-во учеников: ", studentGroup.count)
                    for subject in studentGroup.subjects.keys():
                        print(f"{subject}: {studentGroup.subjects[subject]}")
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