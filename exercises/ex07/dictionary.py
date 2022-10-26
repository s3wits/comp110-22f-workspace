"""Dictionary Functions."""

__author__ = "730555430"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Function inverts a dictionary."""
    result: dict[str, str] = {}
    for key in original:
        if original[key] in result:
            raise KeyError("You cannot have duplicate keys!")
        result[original[key]] = key
    return result


def favorite_color(naco: dict[str, str]) -> str:
    """Function returns the most popular color."""
    repeats: dict[str, int] = {}
    for key in naco:

        if naco[key] in repeats:
            repeats[naco[key]] += 1
        else:
            repeats[naco[key]] = 1
    largest: int = 0
    fav_color: str = ""
    for key in repeats:
        if repeats[key] > largest:
            largest = repeats[key]
            fav_color = key
    return fav_color


def count(og: list[str]) -> dict[str, int]:
    """Function counts the number of times a value occurs in a list."""
    counted: dict[str, int] = {}
    for num in og:
        if num in counted:
            counted[num] += 1
        else:
            counted[num] = 1
    return counted


        
