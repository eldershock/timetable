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