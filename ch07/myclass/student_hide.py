#학생 클래스 만들기
class Student:
    def __init__(self, id, name):
        self.__id = id    #학번
        self.__name= name

    def getid(self):
        return self.__id

    def getname(self):
        return self.__name
    def showinfo(self):   #정보출력 메소드
        print(self.__id,self.__name)


s=Student(202,'지우')
s.showinfo()

