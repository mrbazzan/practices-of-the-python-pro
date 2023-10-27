
from datetime import datetime

class Greeter:
    def __init__(self):
        self.now = datetime.now()

    def _day(self):
        return self.now.strftime("%A")

    def _part_of_day(self):
        if self.now.hour < 12:
            return "morning"
        elif self.now.hour < 17:
            return "afternoon"
        else:
            return "evening"

    def greet(self, store):
        print(f"Hi, welcome to {store}")
        print(f"How's your {self._day()} {self._part_of_day()} going?")
        print("Here's a coupon for 20% off!")


Greeter().greet("baz")
