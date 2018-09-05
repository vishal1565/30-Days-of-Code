class printError(Exception):
    pass

class Calculator():
    def __init__(self):
        pass
    def power(self, n, p):
        if n < 0 or p < 0:
            raise printError("n and p should be non-negative")
        else:
            return pow(n, p)