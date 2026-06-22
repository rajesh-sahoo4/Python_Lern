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

# class Test:
#     a=1000
#     @classmethod 
#     def m1(cls):
#         cls.a=2000
#         print(Test.a)

# t=Test()
# t.m1()
# Test.a=300
# t1=Test()
# t1.m1()
# t.m1()
# # instance Method
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def display(self):
#         print('Hi',self.name)
#         print('Your marks are:',self.marks) 
#     def grade(self):
#         if self.marks>60:
#             print('You got First grade')
#         elif self.marks>=50:
#               print('You got Second grade')   
#         elif self.marks>=35:            
#              print('You got third grade')
#         else:
#             print('You are failed')
# s1=Student('Chiku',65)
# s1.display()
# s1.grade()
# s2=Student('Raju',45)

# # setter and Getter method
# class Student1:
#     def setName(self,name):
#       self.name=name
#     def getName(self):
#       return self.name

#     def getMarks(self,marks):
#         self.marks=marks
#     def getMarks(self):
#         return self.marks
# s1=Student1()
# s1.setName('Rajesh')
# print(s1.getName)          

# # class Method
# class Animal:
#     legs=4
#     @classmethod
#     def walk(cls,name):
#         print("{} walks with {} legs".format(name,cls.legs))
# Animal.walk('dog')
# Animal.walk('cat')

# class Test_2: 
#      count=0  #class variable
#      def __init__(self):
#         Test_2.count=Test_2.count+1
#      @classmethod
#     def noOfObject(cls):
#         print('The number of object are ')

'''create a Employee class in 'TCS' Company  
 company name should be common
 employee should have id,name and salary
 cr

'''
class Employee:
    company_name='TCS'  #class variable
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def display_details(self):
          print("Employee Id:",self.emp_id)
          print("Employee Name:",self.name)  
          print("Salary:",self.salary)  
          print("Company:",Employee.company_name)
    @classmethod
    def change_company(cls,new_company):
        cls.company_name=new_company

    
    #Static method         
    @staticmethod
    def company_policy():
        print('Employee must be work 8 hours')

e1=Employee(101,"Rajesh",50000)
e2=Employee(102,"Rakesh",45000)

e1.display_details()
print()
e2.display_details()
print()
Employee.change_company('Wipro')
e1.display_details()
print()
Employee.company_policy()

# polymorphism 
class Dog:
    def sound(self):
       print('voooo....')
class Cat(self):
    def sound(self):
       print('meeo...')
def make_sound(Animal):
    animal.sound()
make_sound(Dog())
make_sound(Cat())
    




