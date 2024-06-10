import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random string of 15 lowercase ASCII letters.

    Returns:
        str: A random string of 15 lowercase ASCII letters.

    Usage:
        print(generate_id())  # Prints a random string like 'abcxyzpqrstudef'
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student with a name, surname, login, active status, and ID.

    The login is automatically generated from the first letter of the name
    and the surname.
    The ID is automatically generated using the `generate_id` function.
    The active status is True by default.

    Attributes:
        name (str): The student's name.
        surname (str): The student's surname.
        login (str): The student's login, generated from the name and surname.
        active (bool): Whether the student is active. True by default.
        id (str): The student's ID, generated using the `generate_id`
        function.

    Usage:
        student = Student(name="John", surname="Doe")
        print(student.name)  # Prints "John"
        print(student.surname)  # Prints "Doe"
        print(student.login)  # Prints "JDoe"
        print(student.active)  # Prints True
        print(student.id)  # Prints a random string like "abcxyzpqrstudef"
    """
    name: str
    surname: str
    login: str = field(init=False)
    active: bool = True
    id: str = field(default_factory=generate_id)

    def __post_init__(self):
        """
        Initializes the login attribute after the object is created.

        The login is generated from the first letter of the name and the
        surname.
        If the name is empty, the login is the same as the surname.

        Raises:
            IndexError: If the name is empty.
        """
        try:
            self.login = self.name[0] + self.surname
        except IndexError:
            self.login = self.surname


def main():
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
