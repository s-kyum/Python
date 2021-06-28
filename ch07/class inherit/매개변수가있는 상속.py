from person import Person
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
"""
class Employee(Person):
    def __init__(self,name,age,id,pay):
        super().__init__(name,age)  #부모꺼 가져오기
        self.id = id
        self.pay = pay

    def getname(self): #캡슐화(정보은닉) - get()메서드 사용
        return self.name

    def getage(self):
        return self.age

    def getid(self):
        return self.id

    def getpay(self):
        return self.pay

e1=Employee('김성겸',20,201401988,250)
print("이름 : ",e1.getname())
print("나이 : ",e1.getage())
print("사번 : ",e1.getid())
print("월급 : ",e1.getpay())

e2=Employee('윈스턴',38,20019382,500)
print("이름 : ",e2.getname())
print("나이 : ",e2.getage())
print("사번 : ",e2.getid())
print("월급 : ",e2.getpay())