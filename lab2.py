from math import sqrt

def findError(x2):
    return abs(x2 - sqrt(5).real)

def findFunctionValue(value):
    return  value ** 2 - 5

def findDerivative(value):
    return 2 * value

def oneTangentMethod():
    x1 = 3 - findFunctionValue(3)/findDerivative(3) 
    return x1 - findFunctionValue(x1)/findDerivative(3)

def secantMethod():
    x1 = 3 - findFunctionValue(3)/findDerivative(3)
    return x1 - findFunctionValue(x1) * (x1 - 3)/(findFunctionValue(x1) - findFunctionValue(3))

def NewtonMethod():
    x1 = 3 - findFunctionValue(3)/findDerivative(3) 
    return x1 - findFunctionValue(x1)/findDerivative(x1)
    
if __name__ == '__main__':
    print('Метод одной касательной: {}, ошибка = {}'  .format(oneTangentMethod(), findError(oneTangentMethod())))
    print('Метод секущих: {}, ошибка = {}' .format(secantMethod(), findError(secantMethod())))
    print('Метод Ньютона: {}, ошибка = {}' .format(NewtonMethod(), findError(NewtonMethod())))