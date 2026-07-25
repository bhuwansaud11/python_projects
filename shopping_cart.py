#Shopping Cart Program

food=[]
prices=[]
total=0

while True:
    item=input("Enter the item you would like to buy(Q to quit): ")
    if item.lower()=="q":
        break
    else:
        price=int(input("Enter the price of the item: "))
        food.append(item)
        prices.append(price)
print("-----YOUR SHOPPING CART-----")
for i in food:
    print(i,end="  ")
for price in prices:
    total=total+price
print()
print("Your total is: ",total)