print("Enter the first number")
num1 = int(input())
print("Enter any math operator [for eg: +, -, *, /]")
op = input()

if op == "+" or op == "-" or op == "*" or op == "/":
    print("Enter the second number")
else:
    print("Enter any valid math operator")
    quit()

num2 = int(input())

if (num1>=0 and num1<=40) and (num2>=0 and num2<=40):
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        print(num1/num2)
    else:
        print("Invalid choice")
else:
    print(num1+num2*num1-num2)