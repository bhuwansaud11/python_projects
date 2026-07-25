#Python Compound Interest Calcualtor

principle=0
rate=0
time=0

while True:
    principle=float(input("Enter the principle: "))
    if principle<0:
        print("Principle cant be less than zero")
    else:
        break

while True:
    rate=float(input("Enter the rate: "))
    if rate<0:
        print("Rate cant be less than zero. ")
    else:
        break

while True:
    time=int(input("Enter the time in years: "))
    if time<0:
        print("Time cant be less than zero")
    else:
        break

print("Principle: ",principle)
print("Rate: ",rate)
print("Time: ",time)

amount=principle*pow((1+rate/100),time)

print(f"Balance after {time} year/s: ${amount:.2f}")