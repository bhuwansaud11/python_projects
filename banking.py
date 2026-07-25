#Banking Program

def withdraw():
    global balance
    amount=int(input("Enter the amount to be withdrawn: "))
    if amount>balance:
        print("Insufficient funds.")
    else:
        balance-=amount
        print(f"Amount withdrawn successfully: {amount}")

def deposit():
    global balance
    amount=int(input("Enter the amount to be deposited: "))
    if amount<0:
        print("That's not a valid input.")
        return 0
    else:

        balance+=amount
        print(f"Amount deposited successfully: {amount}")
        return amount

def show_balance():
    print("Your balance is", balance)

balance=0
is_running=True
def main():
    global is_running
    while is_running:
        print("---Banking System---")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice=int(input("Enter the choice: "))
        match(choice):
            case 1:
                show_balance()
            case 2:
                deposit()
            case 3:
                withdraw()
            case 4:
                print("Thanks for visiting!")
                print("Exitin...")
                is_running=False
            case _:
                print("Invalid choice. Try again")

if __name__ == '__main__':
    main()