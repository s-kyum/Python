class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age

p1=Person("박대양",40)
p2=Person("지우",20)
p3=Person("윈스턴",35)
print(p1.name,p1.age)
print(p3.name,p3.age)