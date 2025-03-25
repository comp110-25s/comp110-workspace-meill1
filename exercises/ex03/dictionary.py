"""Dictionary Functions"""

__author__ = "730733853"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in dictionary:
        value = dictionary[key]
        if value in inverted_dict:
            raise KeyError("Duplicate key found.")
        inverted_dict[value] = key
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequency of each item in a list."""
    frequency_dict: dict[str, int] = {}
    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Finds the most frequently occurring color in a dictionary."""
    color_count: dict[str, int] = {}
    for color in colors:
        if colors[color] in color_count:
            color_count[colors[color]] += 1
        else:
            color_count[colors[color]] = 1
    fav_color: str = ""
    fav_count: int = 0
    for color in color_count:
        if color_count[color] > fav_count:
            fav_color = color
            fav_count = color_count[color]
    return fav_color


def bin_len(word_list: list[str]) -> dict[int, set[str]]:
    """Creates a dictionary of word lengths and words of that length."""
    length_dict: dict[int, set[str]] = {}
    for word in word_list:
        word_len = len(word)
        if word_len in length_dict:
            length_dict[word_len].add(word)
        else:
            length_dict[word_len] = {word}
    return length_dict
