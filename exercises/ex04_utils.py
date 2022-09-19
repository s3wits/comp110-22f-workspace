"""Ex04 - List utilities"""

__author__ = "730555430"

def all(the_list: list[int], the_int: int) -> bool:
   
    contains: bool = False
    counter: int = 0

    while (counter < len(the_list)):
        if the_list[counter] == the_int:
            contains = True
            counter += 1
        else:
            return False
    return True
#done, works

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    biggest: int = 0
    counter: int = 0
    while (counter < len(input)):
        if input[counter] > biggest:
            biggest = input[counter]
            counter += 1
        else:
            counter += 1
    return biggest
# done, works

def is_equal(first: list[int], second: list[int]) -> bool:
    counter: int = 0
    equal: bool = False
    if len(first) != len(second):
        return equal
    while len(first) > counter:
        if first[counter] == second[counter]:
            counter += 1
        else:
            return equal
    equal = True
    return equal