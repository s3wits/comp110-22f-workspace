"""An example of a list utility algorithm"""

# Function with 2 parameters:
#   needle - what we're searching for
#   haystack - what we're searching through
# Return type bool

# Start from first index
# Loop through each index of list
#   Test if equal to needle
#   # Yes! Return True
# Return False

def contains(needle: str, haystack: list[str]) -> bool:

    contains: bool = False
    counter: int = 0
    while (counter < len(haystack)):
        if needle == haystack[counter]:
            return True
        counter +=1
    return False
