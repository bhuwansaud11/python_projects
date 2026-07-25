#Concession Stand Program

menu={"pizza":3.50,
      "burger":2.00,
      "chips":1.00,
      "fries":2.50,
      "pretzel":1.50,
      "popcorn":6.00,
      "soda":2.50,
      "momo":4.00
}

cart=[]
total=0
while True:
    print("--------------------------")
    print("           MENU           ")
    print("--------------------------")
    for keys,values in menu.items():
        print(f"{keys:13}:${values:.2f}")
    item=input("Select an item(q to quit): ")
    if item.lower()=="q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        total+=menu.get(item)
print("-----YOUR CART-----")
for food in cart:
    print(f"{food:9}:${menu.get(food):.2f}")
print("-------------------")
print(f"Your total: ${total:.2f}")