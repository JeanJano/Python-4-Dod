import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    login: str = field(init=False)
    active: bool = True
    id: str = field(default_factory=generate_id)


    def __post_init__(self):
        try:
            self.login = self.name[0] + self.surname
        except IndexError:
            self.login = self.surname


def main():
    student = Student(name = "", surname = "")
    print(student)


if __name__ == "__main__":
    main()
