# i=10
# while i>=1:
#     print(i)
#     i=i-1
# l=1
# while l<=20:
#     if l % 2==0:
#         print(l) 
#         l+=1     
# 1. Print the multiplication table of 8 using while.
# i = 1
# while i <= 10:
#     print("8 x", i, "=", 8 * i)
#     i += 1
# 2. Print the square of numbers from 1 to 10.
# s = 1
# while s <= 10:
#     print(s * s)
#     s += 1
# 3. Count numbers from 1 to 100 divisible by 7.
d = 1
count = 0
while d <= 100:
    if d % 7 == 0:
        count += 1
    d += 1
print(count)
# 4. Check whether a number is palindrome.
num = int(input('Enter your Number'))
temp = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
if temp == rev:
    print("Palindrome")
# 5. Count total characters in a string using while.
# s = input("Enter your characters:")
# i = 0
# count = 0

# while i < len(s):
#     count += 1
#     i += 1
# print(count)
# 6. Count number of vowels in a string using while.
s1='automation'
i=0
count=0
while i <len(s1):
    if s1[i] in 'aeiouAEIOU':
        count+=1
i+=1 
print('vowels:',count)     
# 7. Count uppercase letters in a string.
s=input('Enter a string:')
i=0
count=0

# 8. Count frequency of a specific character.
# 9. Convert all lowercase characters to uppercase using while.

# 10. Reverse a list using while loop.
i=1
while i<=10:
    print('sqaure of 1 to 10:',i)
    i=i+1 