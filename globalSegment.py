import string
import re
import os

symbols = string.punctuation
studentsWorkDaysTime = []

def clear():
    return os.system("cls")

def strHasOnlyLetters(text: str) -> bool:
    for i in text:
        if i.isdigit():
            print("Ошибка: в строке присутсвуют цифры.")
            return False
        elif i in symbols:
            print("Ошибка: в строке присутсвуют посторонние символы.")
            return False
    return True

def dateTimeValidate(durationTime) -> bool:
    if re.match("\\d{2}:\\d{2}-\\d{2}:\\d{2}", durationTime) or durationTime == '0':
        return True
    else:
        print("Ошибка: введите данные согласно форме.")
        return False