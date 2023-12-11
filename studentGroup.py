class StudentGroup:
    groupName = ""
    count = 0
    # workDays = {}
    subjects = {}

    def __init__(self, groupName, count):
        self.groupName = groupName
        self.count = count
        # self.workDays = {"Понедельник": [],
        #         "Вторник": [],
        #         "Среда": [],
        #         "Четверг": [],
        #         "Пятница": [],
        #         "Суббота": []
        #         }


    def fillSubjects(self):
        subjectsCount = int(input("Введите количество предметов: "))
        #исключение на ввод кол-ва предметов 
        for i in range(subjectsCount):
            subject = str(input("Введите название предмета: "))
            count = int(input("Введите количество уроков в неделю по данному предмету: "))
            self.subjects[subject] = count


     
    # def fillWorkDays(self, studentsWorkDaysTime: list()):
    #     for workDay in self.workDays.keys():
    #         lessons = []
    #         for i in range(len(studentsWorkDaysTime)):
    #             lesson = str(input(f"{workDay}, введите {i+1} урок: "))
    #             lessons.append(lesson)
    #         self.workDays[workDay] = lessons