temp=int(input("Enter the temperature: "))
unit=input("Celsius or Fahrenheit(C or F): ")

if unit=="C":
    temp=round((temp*9/5)+32,2)
    unit="F"
    print(f"The Temperature is {temp} {unit}")
elif unit=="F":
    temp=round((temp-32)*5/9,2)
    unit="C"
    print(f"The Temperature is {temp} {unit}")
else:
    print(f"The {unit} is an invalid unit of measurement")