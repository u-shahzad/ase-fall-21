import calculator as c

class FooCalculator:

    #empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m,n)

    def divide(self, m, n):
        return c.divide(m,n)

if __name__ == "__main__":
    x = FooCalculator()
    print(x.sum(4,9))
    print(x.divide(12,2))