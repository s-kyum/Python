#부모클래스
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    pass


if __name__ == "__main__":
    c1=Person("지우",25)
    print(c1.name,c1.age)

    c2=Employee("지우",25)
    print(c2.name,c2.age)

    c3=Employee("윈스턴",38)
    print(c3.name,c3.age)