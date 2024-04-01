import random
import string
from dataclasses import dataclass, field


def generate_id():
    """random string generator"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student"""
    name: str
    surname: str
    active: bool = field(init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """finish to init Students"""
        self.active = True
        self.login = self.name[0] + self.surname
        self.id = generate_id()


def main():
    """Main test."""
    student = Student(name="Edward", surname="agle")
    print(student)
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)


if __name__ == "__main__":
    main()
