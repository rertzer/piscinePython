from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon family
    """
    def __init__(self, first_name, is_alive=True):
        """
        Create a Baratheon family member
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
        
    @property
    def __str__(self):
        """Return a string representation of the character."""
        return str(f"Vector : ({self.first_name})")
    
    def die(self):
        self.is_alive = False


class Lannister(Character):
    """
    Lannister family
    """
    def __init__(self, first_name, is_alive= True):
        """
        Create a Lannister family member
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        return cls(first_name, is_alive)

def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")

if __name__ == "__main__":
    main()
