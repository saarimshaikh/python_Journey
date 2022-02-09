from ast import operator


a = input("Enter the first number: ")
operator = input("Choose the operator (+,-,*,/,%): ")
b = input("Enter the second number: ")
a = int(a)
b = int(b)

if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
elif operator == '%':
    print(a%b)
else:
    print("Operation is invalid please choose again")

