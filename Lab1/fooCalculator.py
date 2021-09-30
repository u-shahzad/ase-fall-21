import lab1 as c

class FooCalculator:

    #empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m,n)

    def divide(self, m, n):
        return c.divide(m,n)

x = FooCalculator()
print(x.sum(4,9))