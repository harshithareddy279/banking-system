"""
def add(a,b):
    return a+b

if __name__ =="__main__":
    a=10
    b=12
    result=add(a,b)
    print(result)


import p12
a=10
res=p12.square_root(a)
print(res)"""
def check_balance():
    print(f"Yout current balance is {balance}")

def deposit():
    global balance
    if amount>0:
         balance +=amount
    else:
        print("Cannot deposit a negative amount")    
    

def withdraw(amount):
    global balance
    balance -=amount
    print("Withdrawing an amount")

balance=0.0
while True:
    print("1.Check your balance")
    print("2.Deposit an amount")
    print("3.Withdraw an amount")
    print("4.Quit")
    choice=input("Enter your choice (1-4): ")
    if choice=='1':
        check_balance()
    elif choice=='2':
        amt=float(input("Enter the amount to deposit: "))
        deposit(amt)
    elif choice=='3':
        withdraw()
    elif choice='4':
        break
    else:
        print("Invalid choice")

print("Thank you for banking with us!")
    
