class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if a == 0 or b == 0:
            return result
        elif b < 0 and a < 0:
            a = -(a)
            b = -(b)
            for i in range(b):
                result = self.add(result,a)
            return result
        elif b < 0:
            for i in range(a):
                result = self.add(result,b)
            return result
        else:
            for i in range(b):
                result = self.add(result, a)
            return result

    def divide(self, a, b):
        result = 0
        if(b == 0):
            return ValueError
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if a < 0:
            while a <= b and a != 0:
                a = self.add(a, b)
                result -= 1
        return result
    
    def modulo(self, a, b):
        while b <= a:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(20, 2))
    print("Example: subtraction: ", calc.subtract(10, 10))
    print("Example: multiplication: ", calc.multiply(-2,-6))
    print("Example: division: ", calc.divide(-20, 2))
    print("Example: modulo: ", calc.modulo(10,3))