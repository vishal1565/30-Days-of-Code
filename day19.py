class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        temp = []
        for i in range(1,n+1):
            if n%i == 0:
                temp.append(i)
            else:
                pass
        return sum(temp)