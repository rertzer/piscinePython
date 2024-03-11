import sys as sys


def main():
    """
    sos.py take a string as argument and print the corresponding morse code.
    The string must contain only alphanumeric characters and spaces.
    """

    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. ",
                    }

    message = ""

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        for letter in sys.argv[1]:
            letter = letter.upper()
            if letter in NESTED_MORSE:
                message = message + NESTED_MORSE[letter]
            else:
                raise AssertionError("the arguments are bad")

        if len(message) > 0:
            message = message[:-1]
        print(message)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
