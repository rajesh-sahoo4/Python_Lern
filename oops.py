# class student:
#     # d=50
#     # print(d)
#     def __init_(self):
#         self.a=10
#         self.b=20

#     def show(self):
#         pass
# t=student()
# t.c=40
# print(t.__dict__)

# def __inti__(self,name,marks):
#     self.name=name
#     self.marks=marks

# # def display(self):

# # static variable
# class Test:
#     a=10
#     def __init__(self): #constroctur
#         Test.b=20 
#     def show(self): #instance method
#         Test.c=30
#     @classmethod
#     def display(cls):  #class method 
#         cls.d=40
#         Test.e=50
#     @staticmethod
#     def static_method(): # static method
#         Test.f=60

# t1=Test()
# print(Test.__dict__)
# # local variable 
# class Test1:
#     def m1(self):
#         a=1000
#         print(a)
#     def m2(self):
#         b=200
#         print(b)
# t=Test1()
# t.m1()            

class Test:
    a=1000
    @classmethod 
    def m1(cls):
        cls.a=2000
        print(Test.a)

t=Test()
t.m1()
Test.a=300
t1=Test()
t1.m1()
t.m1()
# instance Method
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('Hi',self.name)
        print('Your marks are:',self.marks) 
    def grade(self):
        if self.marks>60:
            print('You got First grade')
        elif self.marks>=50:
              print('You got Second grade')   
        elif self.marks>=35:            
             print('You got third grade')
        else:
            print('You are failed')
s1=Student('Chiku',65)
s1.display()
s1.grade()
s2=Student('Raju',45)

# setter and Getter method
class Student1:
    def setName(self,name):
      self.name=name
    def getName(self):
      return self.name

    def getMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
s1=Student1()
s1.setName('Rajesh')
print(s1.getName)          



