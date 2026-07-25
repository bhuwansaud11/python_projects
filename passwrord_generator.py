#Python password generator

import string
import random

def main():
    is_running = True
    while is_running:
        print("----------PASSWORD GENERATOR----------")
        pw_length = int(input("Enter the length of the pw: "))
        if pw_length<=0:
            print("Password length can not be zero or negative...Try again")
            continue
        print("1. Letters")
        print("2. Alphanum")
        print("3. Letters and symbols")
        print("4. Exit")

        choice = int(input("Enter the choice: "))
        match choice:
            case 1:
                chars = string.ascii_letters
            case 2:
                chars = string.ascii_letters+string.digits

            case 3:
                chars = string.ascii_letters+string.punctuation
            case 4:
                print("Thank you for using me>>>")
                is_running=False
            case _:
                print("INVALID option. Try again")
                continue
        if is_running:
            pw = [random.choice(chars) for _ in range(pw_length)]
            print(''.join(pw))
if __name__=="__main__":
    main()