import sys as sys

assert len(sys.argv) > 1, "no argument is provided"
assert len(sys.argv) < 3, "more than one argument is porvided"

number = sys.argv[1]
assert (number[0] == '-' or number[0] == '+' or number.isdigit()) \
        and (len(number) == 1 or number[1:].isdigit()), "argument is not an integer"
number = int(number)

if  number % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")
