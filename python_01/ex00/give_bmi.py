def give_bmi(height, weight):
    """
    Take lists of height and weight as arguments.
    and return the bmi.
    Height, weight and bmi must be int or float.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            AssertionError("bad arguments: lists expected")
        if len(height) != len(weight):
            raise AssertionError("bad arguments: lists of different sizes")
        if (not all(isinstance(x, (int, float)) for x in height)) or \
           (not all(isinstance(x, (int, float)) for x in weight)):
            raise AssertionError("bad arguments: should be int or float")
        return list(map(lambda h, w: w/(h*h), height, weight))

    except AssertionError as msg:
        print(msg)


def apply_limit(bmi, limit):
    """
    Take a list of bmi and a limit as arguments.
    Return a list of boolean: True if bmi above the limit, False else.
    """
    try:
        if not isinstance(bmi, list):
            raise AssertionError("bad arguments: should be a list")
        if not all(isinstance(x, (int, float)) for x in bmi):
            raise AssertionError("bad arguments: should be int or float")
        if not isinstance(limit, (int, float)):
            raise AssertionError("bad arguments: should be int or float")
        return [x > limit for x in bmi]

    except AssertionError as msg:
        print(msg)


def test(height, weight):
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


def main():
    test([2.71, 1.15], [165.3, 38.4])
    test([3, 1], [165, 38])
    test([2.71, 1], [165, 38.4])
    test(["hello", 1.15], ["world", 38.4])


if __name__ == "__main__":
    main()
