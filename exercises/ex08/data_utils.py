"""Dictionary related utility functions."""

__author__ = "730555430"

from csv import DictReader


# Define your functions below

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oritened table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Produce column based table with a specific number of values from a column."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        if num > len(table[column]):
            num = len(table[column])
        i: int = 0
        while i < num:
            values.append(table[column][i])
            i += 1
        result[column] = values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce column based table with a subset of data."""
    result: dict[str, list[str]] = {}
    for item in names:
        result[item] = table[item]
    return result


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column based tables."""
    result: dict[str, list[str]] = {}
    for column in one:
        result[column] = one[column]
    for column in two:
        if column in result:
            result[column] += two[column]
        else:
            result[column] = two[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts frequency of data in a list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
