class Student:
    def __init__(self):
        self.id = int(input("학번:"))
        self.name = input("이름 : ")

    def showinfo(self):
        print(self.id, self.name)

li = []
for i in range(3):
    li.append(Student()) #Student()가 인스턴스로 저장됨

for i in li:
    i.showinfo()