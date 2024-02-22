import sys as sys

try:
    if len(sys.argv) < 2:
        raise AssertionError("no argument is provided")
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is porvided")

    number = sys.argv[1]
    if (not(number[0] == '-' or number[0] == '+' or number.isdigit()) and (len(number) == 1 or number[1:].isdigit())):
        raise AssertionError("argument is not an integer")
    number = int(number)

    if  number % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
except AssertionError as msg:
    print(msg)
