# pratice  qustion of string , list and dictanary
lst = [10, 20, 30, 20, 40]
# Add value 50 at the end of the list.
lst.append(50)
print(lst)

# 2️⃣ Insert 15 at index 1.
lst.insert(1,15)
print(lst)

# 3️⃣ Remove the first occurrence of 20.
lst.remove(20)
print(lst)

# 4️⃣ Count how many times 20 appears.
print(lst.count(20))


# 5️⃣ Find index of value 30.
print(lst.index(30))

# 6️⃣ Reverse the list.
lst.reverse()
print(lst)

# 7️⃣ Sort the list in ascending order.
lst.sort()
print(lst)

tup = (5, 10, 15, 10, 20)
# 8. Count how many times 10 appears in the tuple.
print(tup.count(10))

# 9. Find index of value 15.
print(tup.index(15))
# 10.  Convert tuple into a list.
l=list(tup)
print(l)
# 11. Find length of tuple.
print(len(tup))
dct = {"name": "Ram", "age": 25, "city": "Delhi"}
# 12. Get the value of key "name".
print(dct.get("name"))
# 13.  Add a new key "country" with value "India".
dct['country']='India'
print(dct)
# 14.  Update "age" to 26.
dct["age"]="26"
print(dct)
# 15. Remove key "city".
dct.pop('city')
print(dct)
# 16. Get all keys from dictionary.
print(dct.keys())
# 17. Get all values from dictionary.
print(dct.values())
s = " python is very easy "
# 18. Remove extra spaces from both ends.
print(s.strip(" "))
# 19.  Convert string to uppercase.
print(s.upper())
# 20. Count how many times "is" appears.
print(s.count('is'))
# 21. Replace "easy" with "simple".
print(s.replace("easy","simple"))
# 22.Split the string into words.
print(s.split())

'''Operator'''
# arithmatic operator
a=20
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(b**2)
print(a//b)

# assignment operator
c=a+b
print(c)
c+=10
print(c)
c-=10
print(c)
c*=2
print(c)
c/=2
print(c)
c%=2
print(c)
c**=2
print(c)
c//=2
print(c)
# x=13
# x/=2
# print(x)

# comparison operator
x=25
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

# Logical Operator
x1=10
print(x1<5 and x1==10)
print(x1<4 or x1>3)
print(not(x1>5 and x1<4))

#Membership Operator
fruits=['Apple',"banana",'cherry']
print('cherry' in fruits)
print('pineapple' not in fruits)

s='Python'
print('y' in s)
print('l' in s)
print('s' not in s)

# Identify Operator
a1=10
b1=10
c1=100
c2=105
print(a1 is b1)
print(a1 is not b1)

# condition_statement 
# 30,40,50
# num=int(input("enter your no:-"))
# if num>=30:
#     print('approved')
# elif num>=40:
#    print("yes u eligiable")
# elif num>=50:
#     print("u are welcome")
# else:
#   print("not approved")

# divided 3 and 5

# if a number divisible by 3 ---fizz
# if a number divisible by 5---buzz
# if a number divisible by both 3 and 5---fizzbuzz

# calculate the electricity bill according to the unit
# 0-100 5 per unnit
# 101-200 7 per unit
# 201-300 10 per unit 
# avobe 300 15 per unit
# unit=int(input("enter your unit:-"))

# age=int(input('Enter your age:-'))
# if age >=18:
#   print('you can vote')
# if age >=21:
#     print("you can also vote")
# else: 
#     print('not eligable for voting')    

# even or odd
# numb=int(input("Enter number: "))
# if numb % 2 == 0:
#     print("Even")
# else:
#     print("odd")    



# loop
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
# 4️.Print all odd numbers between 1 and 20.

# 5️.Print the multiplication table of a given number.
mul=5
for  num2 in range(1,11):
    # print(num2)
    print(mul,'X',num2,'=',mul*num2)
    
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
