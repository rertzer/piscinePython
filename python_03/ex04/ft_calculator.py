class calculator:
    """Calculator class performing vector operations."""

    @staticmethod
    def dotproduct(V1, V2):
        """Print the dotproduct of the lists given as arguments."""
        DP = sum(map(lambda v1, v2:  v1 * v2, V1, V2))
        print(f"Dot product is: {DP}")

    @staticmethod
    def add_vec(V1, V2):
        """Print the sum of the two vectors given as arguments."""
        V3 = list(map(lambda v1, v2:  float(v1) + float(v2), V1, V2))
        print(f"Dot product is: {V3}")

    @staticmethod
    def sous_vec(V1, V2):
        """Print the substraction of the two vectors given as arguments."""
        V3 = list(map(lambda v1, v2:  float(v1) - float(v2), V1, V2))
        print(f"Dot product is: {V3}")


def main():
    """Main test."""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
