
class Slug:
    def __init__(self, name):
        self.name = name

    def crawl(self):
        print("slime trail!")

class Snail(Slug):
    def __init__(self, name, shell_size):
        super().__init__(name)
        self.name = name
        self.shell_size = shell_size


def race(gastropod_one, gastropod_two):
    gastropod_one.crawl()
    gastropod_two.crawl()


race(Slug("Geoffrey"), Slug("Ramona"))
race(Snail("Geoffrey"), Snail("Ramona"))

################################################
# Redesigning Snail and Slug as a composition  #
# rather than an inheritance problem.          #
################################################

class Shell:
    size = None

class Snail:
    def __init__(self, name, shell):
        self.name = name
        self.shell_size = shell.size

Snail("Hafsoh", Shell())


