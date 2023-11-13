class Calculator:
    def __init__(self, value=0):
        self.value = value
    def __add__(self, other):
        return Calculator(self.value + other.value)
    def __sub__(self, other):
        return Calculator(self.value - other.value)
    def __mul__(self, other):
        return Calculator(self.value * other.value)
    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError('Cant divide by 0')
        return Calculator(self.value / other.value)

a = int(input('num1'))
b = int(input('num2'))

a = Calculator(a)
b = Calculator(b)

addition = a+b
subtraction = a-b
multiplication = a*b
division = a/b


print(f'addition: {addition.value}')
print(f'subtraction: {subtraction.value}')
print(f'multiplication: {multiplication.value}')
print(f'division: {division.value}')





