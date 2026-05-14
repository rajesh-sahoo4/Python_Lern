# inheritance 
class parent:
    pass
class child:
    pass 

# single inheritance
# 1 
class Animal:
    def sound(self):
        print('Animals make sound')

class dog(Animal):
    def bark(self):
        print('Dog barks')

d=dog()          
d.sound()
d.bark()
# 2
class Person:
    def show_name(self):
        print('Name: rajesh')

class Student(Person):
    def  show_roll(self):
        print('Roll No: 101')

s= Student()
s.show_name()
s.show_roll()

# 3
class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.bark()

# Multiple Inheritance

# 1
class Sports:
    def play(self):
        print("Playing football")

class Academics:
    def study(self):
        print("Studying subjects")

class Student(Sports, Academics):
    pass

s = Student()
s.play()
s.study()

# 2
class Engine:
    def start(self):
        print("Engine starts")

class MusicSystem:
    def play_music(self):
        print("Music playing")

class Car(Engine, MusicSystem):
    pass

c = Car()
c.start()
c.play_music()

# 3
class Teacher:
    def teach(self):
        print("Teaching students")

class Writer:
    def write(self):
        print("Writing books")

class Person(Teacher, Writer):
    pass

p = Person()
p.teach()
p.write()

# multilevel inheritance

# 1
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.eat()
p.bark()
p.weep()

# 2
class Shape:
    def info(self):
        print("This is a shape")

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

class Box(Rectangle):
    def area(self):
        print("Area:", self.l * self.b)

b = Box(4, 5)
b.info()
b.area()