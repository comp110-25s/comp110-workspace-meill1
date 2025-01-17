"""Number of tea bags, treats, and the cost of a tea party"""

__author__ = "730733853"


def main_planner(guests: int) -> None:
    """Printing how many people, tea bags, treats, and how much the party will cost"""

    print("A Cozy Tea Party for " + str(guests) + " people")

    print("Tea Bags: " + str(tea_bags(people=guests)))

    print("Treats: " + str(treats(people=guests)))

    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Number of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """Number of treats needed"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost of tea bags and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
