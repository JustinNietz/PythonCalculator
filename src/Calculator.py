def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a, b):
   a = int(a)
   b = int(b)
   c = b - a
   return c

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self,a,b):
        self.result = subtraction(a, b)
        return self.result
    

# def multiplication(a,b):
#     return float(a) * float(b)
#
# def division(a,b):
#     if float(a) is not float(0):
#         return round(float(b) / float(a),9)
#     else:
#         return 'Divisor can not be zero.'
#

# def square(a):
#     return float(a)**2
#
# def square_root(a):
#     return round(float(a) ** (1 / 2.0),7)


    # def add(self,a,b):
    #     self.result = addition(a,b)
    #     return self.result
    #
    # def subtract(self,a,b):
    #     self.result = subtraction(a,b)
    #     return self.result
    #
    # def multiply(self,a,b):
    #     self.result = multiplication(a,b)
    #     return self.result
    #
    # def divide(self,a,b):
    #     self.result = division(a,b)
    #     return self.result
    #
    # def sqr(self,a):
    #     self.result = square(a)
    #     return self.result
    #
    # def sqrt(self,a):
    #     self.result = square_root(a)
    #     return self.result