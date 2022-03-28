#Gif, dili diay global ang function??
print('Submitted by: Dan Joshua M. Tagaan')
print()
print()

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
choice = print('Select an operator: \n A. Add \n B. Minus \ C. Divide \n D. Multiply ')

if choice == 'A':
    def addition(add1, add2):
        return add1 + add2

    print(addition(num1,num2))

elif choice == 'B':
    print(min(num1,num2))
elif choice == 'C':
    print(divide(num1,num2))
elif choice == 'D':
    print(multiply(num1,num2))
else:
    print('Invalid Input')


def minus (min1, min2):
    return min1 - min2

def divide(div1,div2):
    return div1 / div2

def multiply(mul1, mul2):
    return mul1 * mul2
