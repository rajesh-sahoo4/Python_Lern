# '''Decorator function'''
# # 1
# def decor_func(func):
#     def inner(name):
#         print('Good morning')
#         func(name)
#         print('Good night')
#     return inner
# @decor_func
# def greet(name):
#     print('Hello',name)
# greet('sanjay')    

# # 2
# def function_1(func1): #new function created function_1 then put parameter func1=say_hello()
#     def wrapper(): #inner function creating
#         print('Before the function')
#         func1() #call the func1=say_hello data 
#         print('after the function')
#     return wrapper  #return inner function
# @function_1 #link the function_1 into say_hello()
# def say_hello():
#     print('hello')
# say_hello()  
# # 3
# def login_required(func2):
#     def wrapper(user):
#         if user=='admin':
#             print('Access Granted')
#             func2(user)
#         else:
#             print('Access denied')
#     return wrapper  
# @login_required
# def dashboard(user):
#     print("Welcome to Dashboard,", user)          
# dashboard("admin")
# dashboard("guest")

# def function_2():
#     print('hi my name is rajesh')
# function_2() 
# # 4
# def decoor_f(cal):
#    def sub(a,b):
#     min=a-b
#     return min
#    return sub

# @decoor_f
# def cal(a,b):
#   add=a+b
#   return add
# print(cal(10,20))
# print(cal(40,30))

# '''List comphersion'''

# num=[10,-20,30,40,50,-60,-70,80]
# result=[x if x>0 else 0 for x in num]
# print(result)

# names=['raj','amar','Biswajit','Lulu']
# first_letter=[name[0].upper() for name in names]
# print(first_letter)

# ''' Dictionary Comprehension'''

# nums=[1,2,3,4,5,6,7,8,9,10]
# even_num={n:n*n for n in nums if n%2==0}
# print(even_num)

# data={'a':10,'b':15,'c':5,'d':20,'e':18}
# result1={k:v for k,v in data.items() if v>=15}
# print(result1)

# num2=[10,11,12,-15,16,-17,-18,-19,20]
# square_data={x:x*x for x in num2 if x>0}
# print(square_data)

# fruit={'a': 'apple', 'b': 'ball', 'c': 'mango'}
# length_f={k:len(v) for k,v in fruit.items()}
# print(length_f)

# key=['a','b','c','d']
# values=[10,20,30,40]
# dict_data={k:v for k,v in zip(key,values)}
# print(dict_data)


# numric=int(input('enter a number:-'))
# print('even' if numric%2==0 else 'odd') 

# '''List Comphersion'''
# lst=[1,2,3,4,5,6,7,8,9]
# lst_r=[x if x%2==0 else x*2 for x in lst if x>2]
# print(lst_r)

# l=[0,1,2]
# pairs=[(i,j) for i in l for j in l if i!=j]
# print(pairs)

# lst2=[1,2,3,4,5] #output=['one','Even','odd','Even','odd']
# result2=['one' if n ==1 else 'Even' if n%2==0 else 'odd' for n in lst2 ]
# print(result2)

# Lst3 = [[1,2,3], [4,5], [6]] #[2, 4, 6]
# result_3 = [x[1] if len(x) == 3 else x[0] for x in Lst3]
# print(result_3)

# lst4 = ['a','b','c','d','a','a','b','c','e']
# freq = {x: lst4.count(x) for x in lst4}
# print(freq)

# l=[1,2,3,4,5,1,2,6,7]

# import copy
# l1=[10,20,[30,40]]
# l2=copy.deepcopy(l1)


# l2[2][0]=99
# print(l2)
# print(l1)

# shallow copy 
import copy 
orginal =[[1,2],[3,4]]
shallow=copy.copy(orginal)
shallow[0][0]=105

print('Original:',orginal)
print('Shallow:',shallow)

# deep copy 
orginal_1=[[1,2],[3,4]]
shallow_1=copy.deepcopy(orginal_1)
shallow_1[0][0]=105

print('Original:',orginal_1)
print('Shallow:',shallow_1)


# import copy

# lst1 = [1, 2, [3, 4]]
# lst2 = copy.copy(lst1)

# lst2[2] = [100, 200]

# print(lst1)
# print(lst2)



















