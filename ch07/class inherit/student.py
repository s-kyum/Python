from person import Person
#Student 클래스 - 학번
class Student(Person):
    def __init__(self,name,age,sid):
        super().__init__(name,age)
        self.sid = sid
    def showinfo(self):
        print(self.name,self.age,self.sid)

s1 = Student("김성겸",20,201401988)
s1.showinfo()