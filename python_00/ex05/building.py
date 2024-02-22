import sys


def text_analyser(text=None):
    if not text:
        print("What is the text to count?")
        for line in sys.stdin:
            text = line
            break
    if not isinstance(text, str):
        print("ERROR (argument is not a string)")
        sys.exit()
    print("The text contains", len(text), "characters:")
    up = 0
    lw = 0
    pu = 0
    sp = 0
    dg = 0
    for x in text:
        if x.isupper():
            up += 1
        elif x.islower():
            lw += 1
        elif x.isspace():
            sp += 1
        elif x.isdigit():
            dg += 1
        elif x in ('.', ',', ';', ':', '?', '!'):
            pu += 1
    print(up, " upper letters")
    print(lw, " lower letters")
    print(pu, " punctuation marks")
    print(sp, " spaces")
    print(dg, " digits")


def main():
    """Given a string as argument, count the number of upper letters, lower
    letters, punctuation marks, spaces and digits. If no string is provided,
    reads on stdin. In this case the final endline will unfortunatly be
    counted. This behavior can easily be avoided, but expected by the subject
    :("""
    
    try:
        if len(sys.argv) > 2:
            raise AssertionError("to many arguments")

        if len(sys.argv) == 1:
            text_analyser(None)
        else:
            text_analyser(sys.argv[1])
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
