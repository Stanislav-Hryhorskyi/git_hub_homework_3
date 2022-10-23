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


def sin_num(x: float) -> str:
    return f"The sine of a number: sin(X) = {math.sin(x)}"


def cos_num(x: float) -> str:
    return f"The cosine of a number: cos(X) = {math.cos(x)}"


def tg_num(x: float) -> str:
    return f"The tangent of a number: tg(X) = {math.tan(x)}"


def asin_num(x: float) -> str:
    return f"The arc-sine of a number: arcsin(X) = {math.asin(x)}"


def acos_num(x: float) -> str:
    return f"The arc-cosine of a number: arccos(X) = {math.acos(x)}"


def atg_num(x: float) -> str:
    return f"The arc-tangent of a number: arctg(X) = {math.atan(x)}"


def log_10_num(x: float) -> str:
    if x < 0:
        return f"The decimal logarithm of a negative number \'X = {x}\' does not exist!"
    else:
        return f"The decimal logarithm of a number: log(X) = {math.log10(x)}"


def ln_num(x: float) -> str:
    if x < 0:
        return f"The natural logarithm of a negative number \'X = {x}\' does not exist!"
    else:
        return f"The natural logarithm of the number: ln(X) = {math.log(x)}"


marker = True
while marker:
    print("""Select the number of the math operation: 
\t1. The addition of two numbers (X + Y);
\t2. The subtraction of two numbers (X - Y);
\t3. The multiplication of two numbers (X * Y);
\t4. The division of two numbers (X / Y);
\t5. The exponentiation of two numbers (X ** Y);
\t6. The square root of a number (X ** 0.5);
\t7. The cube root of a number (X ** (1/3));
\t8. The sine of a number sin(X);
\t9. The cosine of a number cos(X);
\t10. The tangent of a number tg(X);
\t11. The arc-sine of a number arcsin(X);
\t12. The arc-cosine of a number arccos(X);
\t13. The arc-tangent of a number arctg(X);
\t14. The decimal logarithm of a number log(X);
\t15. The natural logarithm of the number ln(X)""")

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
    elif operation_number in range(6, 16):
        try:
            one_number = float(input('Enter a number:  X = '))
        except ValueError:
            if operation_number in (6, 14, 15):
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
        case 8:
            print(sin_num(one_number))
        case 9:
            print(cos_num(one_number))
        case 10:
            print(tg_num(one_number))
        case 11:
            print(asin_num(one_number))
        case 12:
            print(acos_num(one_number))
        case 13:
            print(atg_num(one_number))
        case 14:
            print(log_10_num(one_number))
        case 15:
            print(ln_num(one_number))

    if input('Enter \'off\' to end the program: ').lower() == 'off':
        marker = False
