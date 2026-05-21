# l1=[12,13,14,15,16,28,38,46,50]
# # def show_elements(lst):
# #     for i in lst:
# #         print(i)

# # l1 = [12,13,14,15,16,28,38,46,50]
# # show_elements(l1)

# def fetch_list(l):
#     for i in l:
#         print(i)
#         fetch_list([12,13,14,15,16,28,38,46,50])

# # s1='aaabbcdd' output-{'a':3,'b':2,'c':1,'d':2}
# def count_chars(s):
#     result = {}
    
#     for ch in s:
#         if ch in result:
#             result[ch] += 1
#         else:
#             result[ch] = 1
            
#     return result

# s1 = 'aaabbcdd'
# print(count_chars(s1))
# # s1='aaabbcdd' first non repecting character o/p='c'
# def first_non_repeating(s):
#     freq = {}
    
#     # Step 1: Count frequency
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1

#     # Step 2: Find first non-repeating
#     for ch in s:
#         if freq[ch] == 1:
#             return ch

# s1 = 'aaabbcdd'
# print(first_non_repeating(s1))

# 
names=['ram','tree','deepika','amir']
result=list(map(lambda x:x.upper(),names))
print(result) 

l1=[2,35,21,8,10,15,20,1,29,42]
result1=filter(lambda y:y>15,l1)
print(list(result1))


# write in list comphresion for odd numbers  
# input=[11,12,14,16,18,25,26]
num=[11,12,14,16,18,25,26]
odd_num=[n for n in num if n%2 != 0]
print(odd_num)

# numbers which greater than the 40 print them
# input=[18,25,26,77,10,54,41]
numbs=[18,25,26,77,10,54,41]
gret_num=[]

# remove vowels from a SyntaxWarning
# s1='automation'

# reverse a string s1='programming'

# find the first letter of the inputs
# words=['apple','banana','orange','mango'] output=['a','b','o','m']

# remove negative numbers
# input=[11,-12,14,16,-18,25,26]

# filter name staring with 'A'
# NAMES=['Susree','Vagya','ankush','kanha','Arpita']



# write dict comprehension convert a list to dict where name is key  length of a string 
# names=['ram','prasad','hari','gopal']
# result_dict={name:len(name) for name in names}
# print(result_dict)
# # swap the key and Value
# # date={'a':3,'b':5,'c':7}
# # find cube of numbers
# number=[1,2,3,4,5]
# nums_cube={n:n**3 for n in number}
# print(nums_cube)

#even and odd mapping 
# num_dict=[10,20,24,25,33,26,30]
# result_evod={l:'even' if l%2 == 0 else 'odd' for l in num_dict}
# print(result_evod)

# 
# student=['Ankush','shiv','kanha','khusi','dibya']
# marks=[80,50,65,25,43,15]


# write a function using generator to print even number
# def even_num(n):
#     for  i in range(1,n):
#         if i%2==0:
#             yield i
# n=int(input('Enter your number:'))
# e=even_num(n)
# for i in e:
#     print(i)

# generate sqaure a number

# vowel generator in a string ,input ='automation'
# reverse string  Generator

# def display():
#     print('hello')
# Decorator


def decor_1(func):
    def wrapper(a,b):
        print('Numbers are:',a,b)
        return func(a,b)
    return wrapper    

@decor_1
def  add_value(a,b):
    return a+b
print(add_value(10,20))

# check even and odd
# output:Even number
# number is 10

# multipication started 
# multipication result:200

# recursive function example
 
def desc_num(n):
    if n==0:
        return   #base condition
    print(n)
    desc_num(n-1) #recursive call
desc_num(5)       

#2 write a recursive function for print the factorial of 10

def fact(x):
    if x ==1:
        return 1
    return x*fact(x-1)
print(fact(10))
