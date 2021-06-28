#학생 클래스 만들기
class Student:
    def __init__(self, id, name):
        self.id = id    #학번
        self.name= name
    def showinfo(self):   #정보출력 메소드
        print(self.id,self.name)

if __name__ == "__main__":  #메인에서는 실행되지 않음
    s1=Student(1001,'박대양')
    s2=Student(1002,'이산')
    s1.showinfo()
    s2.showinfo()