class calculator:
    """Vector class on which only scalar calculations can be done."""

    def __init__(self, vector):
        """Class constructor"""
        self.vector = vector

    def __add__(self, number):
        """Addition operator: add a vector and a scalar."""
        self.vector = list(map(lambda v: v + number, self.vector))
        print(self.vector)

    def __mul__(self, number):
        """Multiplication operator: multiply a vector and a scalar."""
        self.vector = list(map(lambda v: v * number, self.vector))
        print(self.vector)

    def __sub__(self, number):
        """Substraction operator: substract a scalar from a vector."""
        self.vector = list(map(lambda v: v - number, self.vector))
        print(self.vector)

    def __truediv__(self, number):
        """True divison operator: divide a vector by a scalar."""
        try:
            if (number == 0):
                raise AssertionError("Division by zero")
            self.vector = list(map(lambda v: v / number, self.vector))
            print(self.vector)
        except AssertionError as e:
            print(e)


def main():
    """Main test."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    v3 / 0


if __name__ == "__main__":
    main()
