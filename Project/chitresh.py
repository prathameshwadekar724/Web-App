
import random as rd
def create_variable(value):
    list=['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
    name = rd.choice(list)
    return value

def add(num1, num2):
    sum=num1+num2
    return sum

def sub(num1, num2):
    minus=num1-num2
    return minus

def mul(num1,num2):
    multiply=num1*num2
    return multiply

def div(num1, num2):
    divide=num1//num2
    return divide

a = float(input("First Value: "))

print("Choose any one Operator(+,-,*,/)")

while True:
    op = str(input("Enter the operator: "))
    if op == "+" or op == "-" or op == "*" or op == "/":
        break
    else:
        print("Invalid Choose Correct Operator")
        continue
if op == '+':
    print("Operator Selected is +")
elif op == '-':
    print("Operator Selected is -")
elif op == '*':
    print("Operator Selected is *")
else:
    print('Operator Selected is /')

z = create_variable(float(input("Enter the second value:")))
print('First Value: ',a)
print('Second Value: ',z)

if op == '+':
    x=add(a,z)
    print("Sum is",x)
elif op == '-':
    y=sub(a,z)
    print("Answer is",y)
elif op == '*':
    u=mul(a,z)
    print("Answer is",u)
elif op == '/':
    w=div(a,z)
    print("Answer is",w)
