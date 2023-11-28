# supports dynamically creating new types
import types


class Strategy:
    """Abstract strategy"""

    def __init__(self, function=None):
        self.name = "Default Strategy"
        # if function is provided, replace strategy
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print(f"{self.name} method is used")


def strategy_one(self):
    print(f"{self.name} is used to execute method 1")


def strategy_two(self):
    print(f"{self.name} is used to execute method 2")


s = Strategy()
s.execute()

s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()