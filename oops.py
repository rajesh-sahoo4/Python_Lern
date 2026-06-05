class student:
    # d=50
    # print(d)
    def __init_(self):
        self.a=10
        self.b=20

    def show(self):
        pass
t=student()
t.c=40
print(t.__dict__)

def __inti__(self,name,marks):
    self.name=name
    self.marks=marks

# def display(self):

# static variable
class Test:
    a=10
    def __init__(self): #constroctur
        Test.b=20 
    def show(self): #instance method
        Test.c=30
    @classmethod
    def display(cls):  #class method 
        cls.d=40
        Test.e=50
    @staticmethod
    def static_method(): # static method
        Test.f=60

t1=Test()
print(Test.__dict__)

