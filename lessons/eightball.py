from random import randint

question: str = input("Ask a yes/no question...")
response: int = radint(0, 3)

if response == 0:
    print("Yes, definitely")
elif response == 1:
    print("ask again later")
elif respone == 2:
    print("My sources say no")
else:
    print("You betcha")
    