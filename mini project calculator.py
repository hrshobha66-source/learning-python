#calculator
a = float(input("Enter the 1st num:"))
b = float(input("Enter the 2nd num:"))
ope = input("Enter operator(+,-,*,/,%,**):")

if ope == '+':
    print(a+b)
elif ope == '-':
    print(a-b)
elif ope == '*':
    print(a*b)
elif ope == '/':
    print(a/b)
elif ope == '%':
    print(a%b)
elif ope == '**':
    print(a**b)
else:
    print("INVALID OPERATION")