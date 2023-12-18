import string
import re
import os

symbols = string.punctuation
studentsWorkDaysTime = ["08:00-08:40", "08:50-09:30", "09:40-10:20", "10:25-11:45", "11:50-12:30", "12:40-13:10"]
workDaysConst = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

def clear():
    return os.system("cls")


#error checkers
def strHasOnlyLetters(text: str) -> bool:
    for i in text:
        if i.isdigit():
            print("Ошибка: в строке присутствуют цифры.")
            return False
        elif i in symbols:
            print("Ошибка: в строке присутствуют посторонние символы.")
            return False
    return True


def strIsInt(text: str) -> bool:
    if text.isdigit():
        return True
    print("Ошибка: число содержит посторонние символы.")
    return False


def dateTimeValidate(durationTime, isLessonsTime = False) -> bool:
    if re.match("\\d{2}:\\d{2}-\\d{2}:\\d{2}", durationTime) or (durationTime == '0' and not isLessonsTime):
        return True
    else:
        print("Ошибка: введите данные согласно форме.")
        return False