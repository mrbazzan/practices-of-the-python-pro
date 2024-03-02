
class Tire:
    def __repr__(self):
        return "A rubber tire"

class Frame:
    def __repr__(self):
        return "An aluminium frame"

class Bicycle:
    def __init__(self):
        self.front_tire = Tire()
        self.back_tire = Tire()
        self.frame = Frame()

    def specs(self):
        print("Front tire: ", self.front_tire)
        print("Back tire: ", self.back_tire)
        print("Frame: ", self.frame)


bicycle = Bicycle()
bicycle.specs()

###########
# BECOMES #
###########

class Bicycle:
    def __init__(self, front_tire, back_tire, frame):
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def specs(self):
        print("Front tire: ", self.front_tire)
        print("Back tire: ", self.back_tire)
        print("Frame: ", self.frame)


bicycle = Bicycle(Tire(), Tire(), Frame())
bicycle.specs()


###########
# TO DO   #
###########

class CarbonFiberFrame:
    def __repr__(self):
        return "A carbon fiber frame"


bicycle = Bicycle(Tire(), Tire(), CarbonFiberFrame())
bicycle.specs()

