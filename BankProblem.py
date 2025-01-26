

def show_balance():
    print("*********************")
    print(f"your balance is {balance:.2f}")

def deposit():
    amount = float(input("enter amount to be deposited: "))
    if amount < 0:
        print("Thats not a valid amount: ")
        return 0
    elif amount < 100:
        print("Amount should be atleast 100:")
        return 0
    else:
        print("Balance is ", balance+amount)
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdraw: "))
    if amount > balance:
        print("insufficent funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print(amount,"rs withdraw sucessfull :)")
        print("Remaining amount is: ", balance-amount)
        return amount

balance = 0
is_running = True

while is_running:
    print("*********************")
    print("---Banking Program---")
    print("1.Show Balance")
    print("2.Depostit")
    print("3.Withdraw")
    print("4.Exit")
    choice = input("Enter your choice (1-4):")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Enter valid choice")

print("Thank you for banking:)")