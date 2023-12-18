class StudentGroup:
    groupName = ""
    count = 0
    subjects = {}
    info = {}

    def __init__(self, groupName, subjects, count):
        self.groupName = groupName
        self.count = count
        self.subjects = subjects


    def fillSubjects(self):
        subjectsCount = int(input("Введите количество предметов: "))
        #исключение на ввод кол-ва предметов 
        for i in range(subjectsCount):
            subject = str(input("Введите название предмета: "))
            hours = int(input("Введите количество уроков в неделю по данному предмету: "))
            self.subjects[subject] = hours