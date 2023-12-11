import string
import re
import os


symbols = string.punctuation
studentsWorkDaysTime = []


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