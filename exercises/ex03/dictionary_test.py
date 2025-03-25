import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len

"""Testing Dictionary Functions"""

__author__ = "730733853"


def test_invert():
    """Testing inverting a dictionary"""
    assert invert({"z": "a", "y": "b", "x": "c"}) == {"a": "z", "b": "y", "c": "x"}


def test_invert_one_item():
    """Testing inverting a dictionary that has one key-value pair"""
    assert invert({"tiger": "lion"}) == {"lion": "tiger"}


def test_invert_error():
    """Testing inverting a dictionary with duplicate values"""
    with pytest.raises(KeyError):
        invert({"a": "z", "b": "y", "c": "z"})


def test_count():
    """Counting the frequency of items in a simple list"""
    assert count(["head", "arm", "arm", "leg", "leg"]) == {
        "head": 1,
        "arm": 2,
        "leg": 2,
    }


def test_count_nothing():
    """Counting the frequency of items in an empty list"""
    assert count([]) == {}


def test_count_unique():
    """Counting the frequency of items in a list that contains all unique items"""
    assert count(["one", "two", "three"]) == {"one": 1, "two": 1, "three": 1}


def test_fav_color():
    """Finding the most common favorite color"""
    assert favorite_color({"James": "red", "Jimmy": "green", "Jim": "red"}) == "red"


def test_one_fav_color():
    """Testing just the favorite color of a dictionary of just one person"""
    assert favorite_color({"James": "red"}) == "red"


def test_tied_fav_color():
    """When the most common favorite color is tied, return the first one that appears"""
    assert favorite_color({"James": "blue", "Jimmy": "green", "Jim": "red"}) == "blue"


def test_bin_len():
    """Grouping words by their lengths"""
    assert bin_len(["apple", "banana", "plum"]) == {
        4: {"plum"},
        5: {"apple"},
        6: {"banana"},
    }


def test_repeating_bin_len():
    assert bin_len(["car", "truck", "dog", "cat"]) == {
        3: {"car", "dog", "cat"},
        5: {"truck"},
    }


def test_no_bin_len():
    assert bin_len([]) == {}
