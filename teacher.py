from globalSegment import dateTimeValidate

class Teacher:
    workDays = {}
    name = ""
    subject = ""


    def __init__(self, name, subject, workDays):
        self.name = name
        self.subject = subject
        self.workDays = workDays
        # self.workDays = {"Понедельник": ["", ""],
        #         "Вторник": ["", ""],
        #         "Среда": ["", ""],
        #         "Четверг": ["", ""],
        #         "Пятница": ["", ""],
        #         "Суббота": ["", ""]
        #         }


    def fillWorkDays(self):
        for workDay in self.workDays.keys():
            while True:
                workTime = str(input(f"{workDay}: введите длительность рабочего дня (форма ввода: XX:XX-XX:XX). Если в этот день работы нет, введите 0\n"))
                if dateTimeValidate(workTime):
                    break
            if workTime == '0':
                self.workDays[workDay] = [workTime]
            else:
                self.workDays[workDay][0] = workTime.split('-')[0]
                self.workDays[workDay][1] = workTime.split('-')[1]
                print(workTime.split('-')[1])
            print(self.workDays[workDay])