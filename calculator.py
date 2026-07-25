# #Pyton Calculator

# def calculator():
#     print("=====Simple Calculator====")
#     n1=int(input("Enter the number 1 : "))
#     n2=int(input("Enter the number 2: "))
#     op=input("Enter the operation to be performed: ")
#     match op:
#         case "+":
#             result=n1+n2
#             return result
#         case "-":
#             result=n1-n2
#             return result
#         case "*":
#             result=n1*n2
#             return result
#         case "/":
#             result=n1/n1
#             return result
#         case "%":
#             result=n1%n1
#             return result
#         case _:
#             return "Invalid operation...."
# while True:
#     print(calculator())
#     repeat=input("Calculate again?(yes or no): ")
#     if repeat.lower()=="no":
#         print("Thanks for using me.....")
#         break


def add(x,y):
    return x+y
def multiply(x,y):
    return x*y

op={
    "+":add,
    "*":multiply
}
ask=input("Enter the op: ")
a=int(input("Enter the n1:"))
b=int(input("Enter the n2: "))
if ask in op:
    result=op[ask](a,b)
    print(result)
else:
    print("Invalid operation")
