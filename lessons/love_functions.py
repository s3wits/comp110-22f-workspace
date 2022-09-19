"""Some tender, loving functions."""


def love (subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}"

print(love("Sarah"))

def spread_love (to: str , n: int) -> str:
    """Generates a str repeating a loving message n time."""
    love_note: str = ""
    counter: int = 0
    while (counter < n):
        love_note += love(to) + "\n"
        counter += 1
    return love_note

print(spread_love("Sarah", 100000))