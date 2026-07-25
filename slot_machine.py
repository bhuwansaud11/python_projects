#Python Slot Machine

import random


symbols=["🍒", "🍋", "🍇", "🍀", "💎"]
balance=100

def spin_rows():
    global symbols
    return [random.choice(symbols) for _ in range(3)]

def join_row(row):
    print("*************************")
    print(" | ".join(row))
    print("*************************")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*2
        elif row[0]=='🍋':
            return bet*4
        elif row[0]=='🍇':
            return bet*6
        elif row[0]=='🍀':
            return bet*10
        elif row[0]=='💎':
            return bet*20
    return 0
def main():
    
    print("Welcome To Slot Machine")
    print("*************************")
    print("Symbols: 🍒 🍋 🍇 🍀 💎")
    print("*************************")
    global balance
    while balance>0:
        if balance <= 0:
            print("You have no more balance. Game over.")
            break

        print(f"Current Balance: {balance}")

        bet=input("Place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number: ")
            continue
        bet=int(bet)
        if bet>balance:
            print("Insufficient Funds!!!")
            continue
        elif bet<=0:
            print("Please enter a valid amount: ")
            continue

        balance-=bet

        row=spin_rows()
        print("Spinning....\n")
        join_row(row)
        payout=get_payout(row,bet)
        if payout>0:
            print(f"You won: ${payout}")
        else:
            print("Sorry. You lost this round")

        balance+=payout

        play_again=input("Do you want to spin again(Y or N): ").upper()
        if play_again!="Y":
            break

    print(f"Final Balance: {balance}")
    
main()