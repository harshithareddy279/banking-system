balance=0.0

def checkbal():
    print(f"Your current balance is {balance}")
def deposit(amount):
    global balance
    if amount>0:
       balance+=amount
    
    else:
        print("Cannot deposit a negative or zero amount.")

def withdraw(amount):
    global balance
    if amount<=0:
        print()
        print("Cannot withdraw a negative or zero amount.")
    elif amount>balance:
        print()
        print("Cannot Withdraw.Insuffient amount.")
    else:
        balance-=amount

if __name__=="__main__":
    print("==========================")
    print("Welcome to the ABC Bank")
    print("==========================")
    
    while True:
        print("1.Check Your Balance")
        print("2.Deposit an amount")
        print("3.Withdraw an amount")
        print("4.Quit")
        print("==========================")
        choice=input("Enter your choice(1-4): ")
        print()
        if choice=='1':
            checkbal()
            print("==========================")
        elif choice=='2':
            amt=float(input("Enter an amount to deposit: "))
            deposit(amt)
            print()
            print(f"Amount {amt} deposited successfully.")
            print("==========================")
        elif choice=='3':
            amt=float(input("Enter an amount to withdraw: "))
            withdraw(amt)
            print()
            print(f"Amount {amt} withdrawn successfully.")
            print("==========================")
        elif choice=='4':
            print("Quitting.Have a great day!")
            break
        else:
            print("Invalid Input")

    print("==========================")
    print("Thank you for banking with us!!")
