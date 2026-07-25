#2D Keypad

num_pad=((1,2,3),
         (3,4,5),
         (7,8,9),
         ("*",0,"#"))

for i in num_pad:
    for j in i:
        print(j,end="  ")
    print()