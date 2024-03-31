from abc import ABC, abstractmethod


class Character(ABC):
    """
    An abstract class for characters.
    """
    def __init__(self, first_name, is_alive=True):
        """
        create chararcter>
        Parameters:
            first_name (string)
            is_alive (boolean, default=True)
        """
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method.
        Supposed to kill someone.
        """
        pass


class Stark(Character):
    """
    A class for the Stark family.
    Inherit from Character.
    """
    def die(self):
        """
        kill a Stark.
        """
        self.is_alive = False


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    rickon = Stark(True, 'pouet')
    print(rickon.__dict__)
    # hodor = Character("hodor")


if __name__ == "__main__":
    main()
