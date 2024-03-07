import sys as sys
import ft_filter as ft


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if not sys.argv[2].isdigit(): 
            raise AssertionError("the arguments are bad")

        words = sys.argv[1].split()
        max_size = int(sys.argv[2])
        words = ft.ft_filter(lambda w : (len(w) > max_size), words)
        print(list(words))

    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
