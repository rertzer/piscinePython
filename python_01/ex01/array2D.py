import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape and return a
    truncated version according to start and end.
    """
    try:
        if not isinstance(family, list):
            raise AssertionError("bad arguments: not a list")
        if not all(isinstance(family[i], list) for i in range(len(family))):
            raise AssertionError("bad arguments: not a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("bad arguments: not int")
        length = len(family[0])
        if not all(len(x) == length for x in family):
            raise AssertionError("bad arguments: non homogenous array")
        family = np.asarray(family)
        print(f"My shape is : {family.shape}")
        family = family[start:end]
        print(f"My new shape is : {family.shape}")
        return family.tolist()
    except AssertionError as msg:
        print(msg)


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print(slice_me(family, 33, 42))
    print(slice_me(family, 33, 'coconut'))
    print(slice_me([[1, 2, 3], 1, 2], 'coconut', 0))


if __name__ == "__main__":
    main()
