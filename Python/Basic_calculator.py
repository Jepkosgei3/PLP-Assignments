Num1 = input("Enter first number: ")
Num2 = input("Enter second number: ")
operator = input("Enter operator: ")

if operator == "+":
    print(int(Num1) + int(Num2))
elif operator == "-":
    print(int(Num1) - int(Num2))
elif operator == "*":
    print(int(Num1) * int(Num2))
elif operator == "/":
    print(int(Num1) / int(Num2))
else:
    print("Invalid operator")
