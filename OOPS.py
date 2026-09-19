class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("This is the config of the machine: ", self.cpu, self.ram)


com = Computer('i5', 16)
# print(type(com))

comnew = Computer('i9', 32)

# com.config()
# comnew.config()

class ComputerNew:
    def __init__(self):
        self.name = "Harshit"
        self.age = 18

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = ComputerNew()
c2= ComputerNew()

c2.name = "Navin"
c2.age = 20

# print(c1.name)
# print(c2.name)

# print(c1.age)
# c1.update()
# print(c1.age)

# print(id(c1))
# print(id(c2))

# if c1.compare(c2):
#     print('They are the same')
# else:
#     print("They are different")

class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

car1 = Car()
car2 = Car()

car1.mil = 9 

# print(car1.com, car1.mil, car1.wheels)
# print(car2.com, car2.mil, car2.wheels)
     
class Student:

    school = 'School'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return ((self.m1 + self.m2 + self.m3)/3)
    
    def getm1(self):
        return self.m1
    
    def setm1(self, value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info(self):
        print("This is Student class.. in abc module")
    
s1 = Student(30,20,40)
# print(s1.avg())
# print(Student.getSchool())
# print(Student.info(s1))

class StudentNew:

    def __init__(self, name, roll):
        self.name = name 
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)

student1 = StudentNew('Harshit', 33)
# student1.show()

class A:
    def __init__(self):
        print("This is inside init A")

    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")

class B:
    def __init__(self):
        print("This is inside init B")
        # super().__init__()

    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")

# b = B()
# b.feature1()

class C(A, B):
    def __init__(self):
        super().__init__()
        print("This is inside init C")

    def feature5(self):
        return print("feature5 is working")
    
# cnew = C()
# cnew.feature1()

class vscode:
    def execute(self):
        print("Compiling")
        print('Executing')

class custom:
    def execute(self):
        print("Custom Compiler")
        print("Custom Execution")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = vscode()
idecustom = custom()

l1 = Laptop()
# l1.code(ide)
# l1.code(idecustom)

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1, m2)
        return s3
    
stu1 = student(80, 40)
stu2 = student(49, 50)

stu3 = stu2 + stu1
# print(stu3.m1)

class new:
    def add(self, a=None, b=None, c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b 
        else:
            s = a 
        return s 

n = new()
# print(n.add())