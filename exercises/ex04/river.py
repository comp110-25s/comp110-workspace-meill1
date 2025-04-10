"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Remove Fish and Bears that are too old"""
        fish_survivors: list[Fish] = []
        bear_survivors: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                fish_survivors.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                bear_survivors.append(bear)
        self.fish = fish_survivors
        self.bears = bear_survivors

    def remove_fish(self, amount: int) -> None:
        """Remove Fish from the river"""
        for _ in range(0, amount):
            if len(self.fish) > 0:
                self.fish.pop()

    def bears_eating(self) -> None:
        """Simulate Bears eating Fish"""
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Remove Bears that are too hungry"""
        hungry_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                hungry_bears.append(bear)
        self.bears = hungry_bears

    def repopulate_fish(self):
        """Simulate Fish reproducing"""
        for fish in self.fish:
            if len(self.fish) // 2 == 0:
                self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """Simulate Bears having babies"""
        for bear in self.bears:
            if len(self.bears) // 2 == 0:
                self.bears.append(Bear())

    def view_river(self) -> None:
        """Print the current state of the river"""
        print(f"~~~ Day: {self.day} ~~~")
        print(f"Fish: {len(self.fish)}")
        print(f"Bears: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulate one week of life in the river"""
        while self.day < 7:
            self.one_river_day()
