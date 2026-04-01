"""Function"""
# ->def function_name(parameters):
# def greet(name):
#     print('Hello',name)
# greet('raju')

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(sub(num1, num2))
elif choice == 3:
    print(mul(num1, num2))
elif choice == 4:
    print(div(num1, num2))
else:
    print("Invalid choice")