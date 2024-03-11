import sys as sys
import ft_filter as ft


def main():
    """
    filterstring(string, size) -> list
    Return a list of words of string greater than size.
    """
    try:
        if len(sys.argv) != 3:
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
