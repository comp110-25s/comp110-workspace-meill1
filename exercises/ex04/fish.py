"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self) -> None:
        """Simulate one day of life for the Fish"""
        self.age += 1
