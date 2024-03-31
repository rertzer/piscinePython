def square(x):
    if not isinstance(x, (int, float)):
        return
    return x**2

def pow(x):
    if not isinstance(x, (int, float)):
        return
    return x**x

def outer(x, func):
    count = x
    def inner():
        nonlocal count
        count = func(count)
        return count
    return inner


def main():
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
