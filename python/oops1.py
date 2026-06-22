class Student:
    def __init__(self):
        self._mark=50 #protected variable
        self.__clg='GIT' #private  variable
    def get_marks(self):
        print(self.__clg)
        print(self._mark)

# s1=Student()
# s1.get_marks()
s2=Student()
s2.get_marks()

# 2
# class ATM:
#     def __init__(self):
#         self.__balance=10000
#     def deposite(self,amount):
#         if amount>0:
#             self.__balance+=amount 
#         else:
#             print('invalid amount')
#     def withdraw(self,amount):
#         if amount>=0        

class ATM: 
    def __init__(self): 
        self.__balance=10000 
 
    def deposit(self,amount): 
        if amount>0: 
            self.__balance += amount 
            print('Amount deposited successfully') 
        else: 
            print('Invalid Amount') 
 
    def withdraw(self,amount): 
        if amount>self.__balance: 
            print('Insufficent balance') 
 
        elif amount<=0: 
            print('Invalid amount') 
        else: 
            self.__balance -= amount 
            print('Amount withdrawn successfully') 
    def check_balance(self): 
        print('current balance is:',self.__balance) 
 
atm=ATM() 
while True: 
    print("\n1. deposit") 
    print("2. withdraw") 
    print("3. check balance") 
    print("4. Exit") 
    choice=int(input('Enter choice:')) 
    if choice==1: 
        amount=int(input('Enter amount:')) 
        atm.deposit(amount) 
    elif choice==2: 
        amount=int(input('Enter amount:')) 
        atm.withdraw(amount) 
 
    elif choice==3: 
        atm.check_balance() 
    elif choice==4: 
        print("Thank u") 
        break 
    else: 
        print('Invalid choice')