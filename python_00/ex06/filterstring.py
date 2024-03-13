import sys as sys
import ft_filter as ft


def main():
    """
    filterstring take a string and a size (int)  as parameters.
    Return a list of words in the string greater than size.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if not all(x.isalnum() or x.isspace() for x in sys.argv[1]):
            raise AssertionError("the arguments are bad")
        if not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")

        words = sys.argv[1].split()
        max_size = int(sys.argv[2])
        words = ft.ft_filter(lambda w: (len(w) > max_size), words)
        print(list(words))

    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
