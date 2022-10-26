"""EX05 'list' Utility Functions Testing."""

__author__ = 730555430


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_none() -> None:
    """(Use 1) Tests only_evens if the list is has no evens."""
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == list()


def test_only_evens_norm() -> None:
    """(Use 2) Tests a list with even numbers."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(test_list) == list([2, 4])


def test_only_evens_empty() -> None:
    """(Edge) Tests an empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_concat_norm() -> None:
    """(Use 1) Tests adding two regular lists."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_negatives() -> None:
    """(Use 2) Tests adding lists with 0 and negative numbers."""
    list_one: list[int] = [0, -1, -4]
    list_two: list[int] = [-2, 0, 0]
    assert concat(list_one, list_two) == [0, -1, -4, -2, 0, 0]


def test_concat_empty() -> None:
    """(Edge) Tests adding empty lists."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_sub_begin_to_end() -> None:
    """(Use 1) Tests returning a full list."""
    list: list[int] = [1, 2, 3]
    begin: int = 0
    end: int = 3
    assert sub(list, begin, end) == [1, 2, 3]


def test_sub_middle() -> None:
    """(Use 2) Tests returning items in the middle of a list."""
    list: list[int] = [1, 2, 3, 4, 5, 6]
    begin: int = 2
    end: int = 5
    assert sub(list, begin, end) == [3, 4, 5]


def test_sub_end_zero() -> None:
    """(Edge) Tests if parameters are equal to 0, empty list."""
    list: list[int] = [1, 2, 3]
    begin: int = 0
    end: int = 0
    assert sub(list, begin, end) == []