import ft_filter as ft


def even_func(i: int):
    """
    test function. Take an int as param and return True if even, False else.
    """
    if i % 2 == 0:
        return True
    return False


def vowel_func(c):
    if c in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    return False


def main():
    """
    This is a test program for ft_filter.
    It compares ft_filter output to the one of filter.
    """
    numbers = [1, 2, 3, 17, 0, 42]
    string = "Ohhhhhh Macarena"

    try:
        print("The original one:")
        filtered = filter(even_func, numbers)
        print(f"before: {numbers}\nafter:{list(filtered)}")
        print("ft_filter:")
        filtered = []
        filtered = ft.ft_filter(even_func, numbers)
        print(f"before: {numbers}\nafter:{list(filtered)}")

        print("The original one:")
        filtered = filter(vowel_func, string)
        print(f"before: {string}\nafter:{list(filtered)}")
        print("ft_filter:")
        filtered = []
        filtered = ft.ft_filter(vowel_func, string)
        print(f"before: {string}\nafter:{list(filtered)}")

        print("The original one:")
        filtered = filter(None, numbers)
        print(f"before: {numbers}\nafter:{list(filtered)}")
        print("ft_filter:")
        filtered = []
        filtered = ft.ft_filter(None, numbers)
        print(f"before: {numbers}\nafter:{list(filtered)}")

        """
        print("The original one:")
        filtered = filter("coconut", numbers)
        print(f"before: {numbers}\nafter:{list(filtered)}")

        print("ft_filter:")
        filtered = []
        filtered = ft.ft_filter("coconut", numbers)
        print(f"before: {numbers}\nafter:{list(filtered)}")
        """
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
