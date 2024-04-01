def square(x):
    """Return the number given as argument, squared."""
    if not isinstance(x, (int, float)):
        return
    return x**2


def pow(x):
    """Return the number given as argument, exponentiated by himself."""
    if not isinstance(x, (int, float)):
        return
    return x**x


def outer(x, func):
    """Takes as argument a number and a function.
    Return a function that returns the result of
    the arguments calculation."""
    count = x

    def inner():
        nonlocal count
        count = func(count)
        return count
    return inner


def main():
    """Main test."""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
