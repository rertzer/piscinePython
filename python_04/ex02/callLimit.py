def callLimit(limit):
    """Takes as argument a call limit of another function and blocks
    its execution above a limit."""
    count = 0

    def callLimiter(func):
        nonlocal count

        def limit_function(*args, **kwargs):
            nonlocal count
            if count < limit:
                count += 1
                func(*args, **kwargs)
            else:
                print(f"Error: {func} call too many times")

        return limit_function
    return callLimiter


def main():
    """Main test."""

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
