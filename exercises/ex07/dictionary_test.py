"""Dictionary Functions Test File."""


__author__ = "730555430"


from dictionary import invert, favorite_color, count
import pytest


def test_invert_norm() -> None:
    """(Use 1) Test the invert function normally."""
    test_dict: dict[str, str] = {"I'm": "Bad", "At": "This"}
    assert invert(test_dict) == {"Bad": "I'm", "This": "At"}


def test_invert_once() -> None:
    """(Use 2) Test invert with one parameter."""
    test_dict: dict[str, str] = {"one": "two"}
    assert invert(test_dict) == {"two": "one"}


def test_invert_edge() -> None:
    """(Edge) Tests the error message."""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {"one": "one", "two": "one"}
        invert(test_dict)


def test_favorite_color_reg() -> None:
    """(Use 1) Regular use of favorite_color."""
    test_dict: dict[str, str] = {"Sam": "Pink", "Rick": "Blue", "Frank": "Blue"}
    assert favorite_color(test_dict) == "Blue"


def test_favorite_color_one() -> None:
    """(Use 2) Testing favorite color function with one parameter."""
    test_dict: dict[str, str] = {"George": "Black"}
    assert favorite_color(test_dict) == "Black"


def test_favorite_color_edge() -> None:
    """(Edge) Tests the function if there is a tie in colors."""
    test_dict: dict[str, str] = {"Sam": "Blue", "Hannah": "Blue", "Will": "Pink", "Bill": "Pink"}
    assert favorite_color(test_dict) == "Blue"


def test_count_norm() -> None:
    """(Use 1) Regular use of the counter function."""
    test_list: list[str] = ["1", "1", "2", "3", "4", "4"]
    assert count(test_list) == {"1": 2, "2": 1, "3": 1, "4": 2}


def test_count_one() -> None:
    """Tests the count function when there is only 1 number."""
    test_list: list[str] = ["7"]
    assert count(test_list) == {"7": 1}


def test_count_edge() -> None:
    """(Edge) Tests count when they are all the same."""
    test_list: list[str] = ["1", "1", "1", "1"]
    assert count(test_list) == {"1": 4}