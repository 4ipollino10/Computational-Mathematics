import math


def findFunctionalValue(x):
    return math.sin(x)

def findIntegrallBySimpsonMethod(a, b, n):
    h = abs(b - a) / n
    res = 0
    for i in range (0, math.trunc(n/2)):
        res += (findFunctionalValue(a) + findFunctionalValue(a + 2 * h) + 4 * findFunctionalValue(h + a)) * h / 3
        a += 2 * h
    return res

def findIntegrallByTrapezoidMethod(a, b, n):
    h = abs(b - a) / n
    res = 0
    for i in range (0, n):
        res += (findFunctionalValue(a) + findFunctionalValue(a + h)) / 2 * h
        a += h
    return res

if __name__ == '__main__':

    sh100 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 100)
    sh200 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 200)

    sh1000 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 1000)
    sh2000 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 2000)
    
    
    sh1100 = findIntegrallBySimpsonMethod(0, math.pi / 2, 50)
    sh2200 = findIntegrallBySimpsonMethod(0, math.pi / 2, 100)
    
    sh11000 = findIntegrallBySimpsonMethod(0, math.pi / 2, 1000)
    sh22000 = findIntegrallBySimpsonMethod(0, math.pi / 2, 2000)

    sh1200 = findIntegrallBySimpsonMethod(0, math.pi / 2, 200)
    sh2400 = findIntegrallBySimpsonMethod(0, math.pi / 2, 400)

    print("sh100 = ", sh100)
    print("sh200 = ", sh200)
    print("sh1000 = ", sh1000)
    print("sh2000 = ", sh2000)

    print("sh1100 = ", sh1100)
    print("sh2200 = ", sh2200)
    print("sh11000 = ", sh11000)
    print("sh22000 = ", sh22000)

    print("sh1200 = ", sh1200)
    print("sh2400 = ", sh2400)

    print("k_trapezoid1, h = 2pi/50, 2pi/100 =", math.log2(abs(sh100 - 1) / abs(sh200 - 1)))
    print("k_trapezoid2, h = 2pi/100, 2pi/200 =", math.log2(abs(sh1000 - 1) / abs(sh2000 - 1)))

    print("k_simpson1, h = 2pi/50, 2pi/100 =", math.log2(abs(sh1100 - 1) / abs(sh2200 - 1)))
    
    print("k_simpson2, h = 2pi/500, 2pi/10ы00 =", math.log2(abs(sh11000 - 1) / abs(sh22000 - 1)))
    
    print("k_simpson3, h = 2pi/200, 2pi/400 =", math.log2(abs(sh1200 - 1) / abs(sh2400 - 1)))

