print('Submitted by: Dan Joshua M. Tagaan\n\n')

def addition(add1, add2):
    return add1 + add2

def subtract (min1, min2):
    return min1 - min2

def divide(div1,div2):
    return div1 / div2

def multiply(mul1, mul2):
    return mul1 * mul2


while True:
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

        choice = input('Select an operator: \n A. Add \n B. Minus \n C. Divide \n D. Multiply \n : ')
        choice = choice.upper()
        
        if choice == 'A':
            print(str(num1) + ' + ' + str(num2) + ' = ', addition(num1,num2))

        elif choice == 'B':
            print(str(num1) + " - " + str(num2) + " = ", subtract(num1,num2))
            
        elif choice == 'C':
            print(str(num1) + ' / ' + str(num2) + ' = ', divide(num1,num2))

        elif choice == 'D':
            print(str(num1) + ' * ' + str(num2) + ' = ',  multiply(num1,num2))
        else:
            print('Invalid Input')
            raise TypeError
        break
    except Exception as e:
        print(e)

