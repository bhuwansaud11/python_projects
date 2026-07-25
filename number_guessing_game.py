import random

while True:
    print("Welcome to Number Guessing Game!!!")
    print("Choose the difficulty level!!")
    print("1. Easy (1-50), unlimited guesses.")
    print("2. Medium (1-100), 10 guesses.")
    print("3. Hard (1-200), 7 guesses.")
    
    choice=int(input("Enter the choice of difficulty level: "))
    if choice==1:
        secret=random.randint(1,50)
        print("I have picked a random number betrween 1 and 50, Can you guess it!! ")
        print("You got unlimited guesses.")
        attempts=0
        while True:
            guess=int(input("Enter your guess: "))
            attempts+=1
            lowest_num=1
            highest_num=50
            if guess>secret:
                print("Too high! Try lower")
            elif guess<secret:
                print("Too low! Try higher")
            elif guess>highest_num or guess<lowest_num:
                print("The number is out of range.")
                print(f"Please select a number between {lowest_num} and {highest_num}!")
            else:
                print("CORRECT! The answer was ",guess)
                print("You got it in ",attempts," attempts. ")
                break
    elif choice==2:
        secret=random.randint(1,100)
        print("I have picked a random number between 1 and 100, Can you guess it?")
        print("You got 7 guesses!!")
        max_attempts=7
        attempts=0
        for i in range(1,max_attempts+1):
            guess=int(input("Enter your guess: "))
            attempts+=1
            max_attempts-=1
            lowest_num=1
            highest_num=100
            if guess>secret:
                print("Too high. Try lower")
                print(f"You got {max_attempts} attempts left")
            elif guess<secret:
                print("Too low. Try Higher")
                print(f"You got {max_attempts} attempts left.")
            elif guess<lowest_num or guess>highest_num:
                print("The number is out of range. ")
                print(f"Please select a number between {lowest_num} and {highest_num}")
                print(f"You got {max_attempts} attempts left.")
            else:
                print("CORRECT! The answer was",secret)
                print(f"You got it in {attempts} attempts")
                break
            if max_attempts==0:
                print("The secret value was ",secret)

    else:
        secret=random.randint(1,200)
        print("i have picked a random number between 1 and 200. Can you guess it? ")
        print("You got 5 guesses")
        max_attempts=5
        attempts=0
        for i in range(1,max_attempts+1):
            guess=int(input("Enter your guess: "))
            attempts+=1
            max_attempts-=1
            lowest_num=1
            highest_num=200
            if guess>secret:
                print("Too high! Try lower.")
                print(f"You got {max_attempts} attempts left.")
            elif guess<secret:
                print("Too low! Try higher.")
                print(f"You got {max_attempts} attempts left.")
            elif guess<lowest_num or guess>highest_num:
                print("The number is out of range.")
                print(f"Please select a number between {lowest_num} and {highest_num}")
                print(f"You got {max_attempts} attempts left")
                break
            else:
                print("CORRECT! The answer was ",secret)
                print(f"You got it in {attempts} attempts")
                break
            if max_attempts==0:
                print("The secret number was",secret)

    print("Thank you for playing!!")
    
    repeat=input("Do you want to play again?(Yes or No): ")
    if not repeat.lower() =="yes":
        print("Exiting...")
        break