"""
Primitive calculator)
"""


def add_num(x, y: float) -> str:
    return f"The addition of two numbers: X + Y = {x + y}"


def sub_num(x, y: float) -> str:
    return f"The subtraction of two numbers: X - Y = {x - y}"


def mult_num(x, y: float) -> str:
    return f"The multiplication of two numbers: X * Y = {x * y}"


def div_num(x, y: float) -> str:
    if y:
        return f"The division of two numbers: X / Y = {x / y}"
    else:
        return "You cannot divide by zero!!!"


def pow_num(x, y: float) -> str:
    if not x and not y:
        return f"The exponentiation of two zero numbers: X ** Y = {1}"
    elif not x and y < 0:
        return f"You cannot raise zero to a negative power (you cannot divide by zero)!!!"
    else:
        return f"The exponentiation of two numbers: X ** Y = {x ** y}"


def sqrt_num(x: float) -> str:
    if x < 0:
        return f"The square root of a negative number \'X = {x}\' does not exist!"
    else:
        return f"The square root of a number: X ** 0.5 = {x ** 0.5}"


def crt_num(x: float) -> str:
    result = x ** (1 / 3) if x >= 0 else -(abs(x)) ** (1 / 3)
    return f"The cube root of a number: X ** (1/3) = {result}"


marker = True
while marker:
    print("""Select the number of the math operation: 
\t1. The addition of two numbers (X + Y);
\t2. The subtraction of two numbers (X - Y);
\t3. The multiplication of two numbers (X * Y);
\t4. The division of two numbers (X / Y);
\t5. The exponentiation of two numbers (X ** Y);
\t6. The square root of a number (X ** 0.5);
\t7. The cube root of a number (X ** (1/3))""")

    try:
        operation_number = int(input('You select the math operation (sequence number): '))
    except ValueError:
        print("Incorrectly entered data! You must enter an integer from 1 to 7 inclusive")
    if operation_number in range(1, 6):
        try:
            first_number = float(input('Enter the first number:  X = '))
            second_number = float(input('Enter the second number: Y = '))
        except ValueError:
            print("Incorrectly entered data! You need to enter two numbers (integer or floating point)")
            operation_number = 0
    elif operation_number in range(6, 8):
        try:
            one_number = float(input('Enter a number:  X = '))
        except ValueError:
            if operation_number == 6:
                print("Incorrectly entered data! You need to enter a POSITIVE number (integer or floating point)")
            else:
                print("Incorrectly entered data! You need to enter a number (integer or floating point)")
            operation_number = 0
    else:
        print('The number of the mathematical operation was incorrectly selected!')

    match operation_number:
        case 1:
            print(add_num(first_number, second_number))
        case 2:
            print(sub_num(first_number, second_number))
        case 3:
            print(mult_num(first_number, second_number))
        case 4:
            print(div_num(first_number, second_number))
        case 5:
            print(pow_num(first_number, second_number))
        case 6:
            print(sqrt_num(one_number))
        case 7:
            print(crt_num(one_number))

    if input('Enter \'off\' to end the program: ').lower() == 'off':
        marker = False
