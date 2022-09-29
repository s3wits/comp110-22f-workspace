"""EX05 'list' Utility Functions."""

__author__ = 730555430

def only_evens(even: list[int]) -> list[int]:
    """Returns the even numbers in a list."""
    even_list: list[int] = list()
    for number in even:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

def concat(one: list[int], two: list[int]) -> list[int]:
    """Adds two lists together."""
    combined: list[int] = list(one + two)
    return combined

def sub(a_list: list[int], begin: int, end: int) -> list[int]:
    """Returns items in the list"""
    final: list[int] = list()
    counter: int = 0

    if len(a_list) == 0:
        return final

    if begin > len(a_list):
        return final

    if end <= 0:
        return final

    counter: int = 0
    while len(a_list) >= counter:
        if counter < begin:
            counter += 1
        if counter >= begin:
            if counter < end:
                final.append(a_list[counter])
            counter += 1
    return final