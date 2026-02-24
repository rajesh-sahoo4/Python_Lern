# Pratice Question of Condition statement and loops statement

# 1️⃣ Positive, Negative or Zero

# num=int(input("enter your no:-"))
# if num >0:
#     print("Positive")
# elif num <0:
#     print("Negative")    
# else:    
#    print("Zero")

# 2️⃣ Even / Odd + Multiple of 4

# num1=int(input("enter you num:-"))
# if num1 %2 == 0:
#   print("Even")
# elif num1 %4 ==0:
#     print("also multiple of 4")
# else:
#     print("odd")

# 3️⃣ Largest of Three Numbers

# a=int(input("Enter First number:-"))
# b=int(input("Enter Second number:-"))
# c=int(input("enter Third number:-"))
# if a>=b and a>=c:
#     print('Largest Number is:',a)
# elif b>=a and b>=c:
#     print('Largest Number is:',b)
# else:
#     print('Largest Number is:',c)        

# 4️⃣Take age and print:
# Child (0–12),Teen (13–19), Adult (20–59),Senior (60+)

# age=int(input('Enter your age:-'))
# if age<=12:
#     print("Child")
# elif age<=19:
#     print('Teen')
# elif age<=59:
#     print('Adult')
# else:
#     print('Senior')      
      
# 5️⃣Check whether a character is:
# Uppercase letter,Lowercase letter,Digit,Special character

# ch=input('Enter a character: ')
# if ch.isupper():
#     print('Uppercase Letter')
# elif ch.islower():
#     print('Lowercase Letter')
# elif ch.isdigit():
#     print('Digit')
# else:
#     print('Special Character')            

# 6️⃣Login validation:
# Correct username & password → Login success
# Wrong username → Username error,Wrong password → Password error

# username=input('Enter username: ')
# password=input('Enter password: ')
# if username =='Admin' and password =='1234':
#     print('login Success')
# elif username !='Admin':
#     print('Username error')
# else:
#     print('Password error')   
     
# 7️⃣Grade system:
#≥90 → A,≥75 → B,≥60 → C,≥40 → D,<40 → Fail

# mark=int(input('Enter your mark:'))
# if mark >=90:
#     print('Grade A')
# elif mark >=75:
#     print('Grade B')
# elif mark >=60:
#     print('Grade C')
# elif mark>=40:
#     print('Grade D')
# else:
#     print('Fail')       
     
# 8️⃣Find the second largest of three numbers.

# x=int(input('Enter First number:- '))
# y=int(input('Enter second number:-'))
# z=int(input('Enter Third number:-'))
# if x>y and x<z:
#     print('Second Largest is:',x)
# elif y>x and y<z:
#     print('Second Largest is:',y)
# else:
#     print('Second Largest is:',z) 
       
# 9️⃣Traffic light system:
# Red → Stop,Yellow → Ready,Green → Go
# color=input('Enter traffic light color:-')
# if color.lower() =='red':
#     print('Stop')
# elif color.lower() =='yellow':
#     print('Ready')
# elif color.lower() =='green':
#     print('Go')
# else:
#     print('invalid color')            

#🔟Check whether a number is palindrome using conditions.
# num2=input('Enter number: ')
# if num2 == num2[::-1]:
#     print('Palindrome')
# else:
#     print('Not palindrome')    

#11 calculate the electricity bill according to the unit
# 0-100 5 per unnit,101-200 7 per unit,201-300 10 per unit and avobe 300 15 per unit
# units=int(input("enter your unit:-"))
# bill=0
# if units<=100:
#    bill=units*5
# elif units<=200:
#     bill=(100*5)+(units-100)*7 
# elif units<=300:
#     bill=(100*5)+(100*7)+(units-200)*10
# else:
#     bill=(100*5)+(100*7)+(100*10)+(units-300)*15
# print('Total Electricity Bill=',bill)    


#12 divided 3 and 5
# if a number divisible by 3 ---fizz
# if a number divisible by 5---buzz
# if a number divisible by both 3 and 5---fizzbuzz
# num3=int(input("Enter your number:-"))
# if num3%3==0:
#     print("fizz")
# elif num3 % 5==0:
#     print('buzz')
# elif num3 %3==0 and num3%5==0:
#     print('fizzbuzz')
# else:
#     print('not divisible by 3 & 5')         
#13 30,40,50
# num=int(input("enter your no:-"))
# if num>=30:
#     print('approved')
# elif num>=40:
#    print("yes u eligiable")
# elif num>=50:
#     print("u are welcome")
# else:
#    print("not approved")

# 14 
# age=int(input('Enter your age:-'))
# if age >=18:
#   print('you can vote')
# if age >=21:
#     print("you can also vote")
# else: 
#     print('not eligable for voting')  

#15
#  even or odd
# numb=int(input("Enter number: "))
# if numb % 2 == 0:
#     print("Even")
# else:
#     print("odd")     

'''Loops'''
# for i in range(10):
#     print(i)

# for i in range(10):
#     print('a')    

l=[10,20,30,40,50]
n=len(l)
for i in range(n):
    print(i)

s='automation'
for ch in s:
    print(ch)    
mul=5
for  num2 in range(1,11):
    # print(num2)
    print(mul,'X',num2,'=',mul*num2)

# 1️.Print numbers from 1 to 10 using for loop.
for num in range(1,10):
    print(num)

# 2️.Print numbers from 10 to 1 using for loop.
for num1 in range(10,1,-1):
    print(num1)

# 3️.Print all even numbers between 1 and 20.
for ev in range(1,20):
    if ev%2==0:
        print(ev,'even number')
    else:
        print(ev,'odd number')
# 4️.Print all odd numbers between 1 and 20.
# 5️.Print the multiplication table of a given number.
# mul=5
# for  num2 in range(1,11):
#     # print(num2)
#     print(mul,'X',num2,'=',mul*num2)

    # num4=int(input('Enter your number:- '))
    # for mul1 in range(1,11):
    #     print(num4,'X',mul1,'=',num4*mul1)
    
# ##########6.Find the sum of first N natural numbers.

# 7️.Find the factorial of a number using for loop.
# 8️.Count how many numbers are divisible by 3 between 1 and 100.
# 9️.Count the digits in a number using for loop.
# 10.Reverse a number using for loop.
# #########1️1.Check whether a number is prime.
# 1,####️2.Print all prime numbers between 1 and 100.
# 1️3.Check whether a number is Armstrong.
# 1️4.Find the sum of digits of a number.
# 1️5.Check whether a number is palindrome. 
# 16 