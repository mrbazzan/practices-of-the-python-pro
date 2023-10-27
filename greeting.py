
from datetime import datetime

NOW = datetime.now()

def day():
    return NOW.strftime("%A")

def part_of_day():
    if NOW.hour < 12:
        return "morning"
    elif NOW.hour < 17:
        return "afternoon"
    else:
        return "evening"

class Greeter:
    def __init__(self):
        pass

    def greet(self, store):
        print(f"Hi, welcome to {store}")
        print(f"How's your {day()} {part_of_day()} going?")
        print("Here's a coupon for 20% off!")


Greeter().greet("baz")
