# Python Unit Convertor

def length():
        print("--LENGTH MENU--")
        print("1. km to miles")
        print("2. cm to inches")
        value = int(input("Enter the value to get converted: "))
        ask = int(input("Select the conversion type: "))
        
        def toMiles():
            convertedValue = value*0.621371
            print(f"{value} km = {convertedValue} miles")
        def toInches():
            convertedValue = value/2.54
            print(f"{value} cm = {convertedValue} inches")

        match ask:
            case 1:
                toMiles()
            case 2:
                toInches()
            case _:
                print("Invalid choice. Please Try Again.")
                    

def weight():
        print("--WEIGHT MENU--")
        print("1. kg to lbs")
        print("2. grams to ounces")
        value = int(input("Enter the value to get converted: "))
        ask = int(input("Select the conversion type: "))
        def toLBS():
            convertedValue = value*2.20462
            print(f"{value} kg = {convertedValue} lbs")
        def toOunces():
            convertedValue = value/28.3495
            print(f"{value} grams = {convertedValue} ounces")
        
        match ask:
            case 1:
                toLBS()
            case 2:
                toOunces()
            case _:
                print("Invalid choice. Please Try Again.")

def temperature():
        print("--TEMPERATURE MENU--")
        print("1. celsius to fahrenheit")
        print("2. kelvin to celsius")
        value = int(input("Enter the value to get converted: "))
        ask = int(input("Select the conversion type: "))
        def toFahrenheit():
            convertedValue = round((value*9/5)+32,2) 
            print(f"{value}°C = {convertedValue}°F")
        def toCelsius():
            convertedValue = value-273.15
            print(f"{value}K = {convertedValue}°C")
        
        match ask:
            case 1:
                toFahrenheit()
            case 2:
                toCelsius()
            case _:
                print("Invalid choice. Please Try Again.")

def main():
    is_running = True
    while is_running:
        print("--------------------")
        print("   UNIT CONVERTOR   ")
        print("--------------------")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = int(input("Select the type of conversion: "))
        

        match choice:
            case 1:
                length()
            case 2:
                weight()
            case 3:
                temperature()
            case 4:
                print("Thank you for visiting...!!!")
                print("Exiting...")
                is_running = False
            case _:
                print("Invalid choice. Please try again. ")

main()