from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Diamond Monster Class."""

    def set_eyes(self, eyes):
        """A function to set eyes."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """A function to set hairs."""
        self.hairs = hairs

    def get_eyes(self):
        """A function to get eyes."""
        return self.eyes

    def get_hairs(self):
        """A function to get hairs."""
        return self.hairs


def main():
    """main test."""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
