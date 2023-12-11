class StudentGroup:
    groupName = ""
    count = 0
    workDays = {}
    
    def __init__(self, groupName, count):
        self.groupName = groupName
        self.count = count
        self.workDays = {"Понедельник": [],
                "Вторник": [],
                "Среда": [],
                "Четверг": [],
                "Пятница": [],
                "Суббота": []
                }
        
    def fillWorkDays(self, studentsWorkDaysTime: list()):
        for workDay in self.workDays.keys():
            lessons = []
            for i in range(len(studentsWorkDaysTime)):
                lesson = str(input(f"{workDay}, введите {i+1} урок: "))
                lessons.append(lesson)
            self.workDays[workDay] = lessons