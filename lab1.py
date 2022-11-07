
from cmath import sqrt

a, b, c, e, d = (float(input()) for i in 'abced')    
discr = (a * 2) ** 2 - (12 * b)

def findDiscRoots(aCoef = a, bCoef = b):
    x1 = (-aCoef - sqrt((aCoef) ** 2 - (3 * bCoef))) / 3
    x2 = (-aCoef + sqrt((aCoef) ** 2 - (3 * bCoef))) / 3
    getRootsLocation(x1.real,x2.real)

def getRootsLocation(alpha, beta, epsilon = e):
    
    if(findFunctionValue(alpha) > epsilon):
        
        if(findFunctionValue(beta) > epsilon):
            makeStep(alpha, 1)
        elif(findFunctionValue(beta) < -epsilon):
            makeStep(beta, 0)
            findRoot(alpha, beta)
            makeStep(alpha, 1)
        elif(abs(findFunctionValue(beta)) < epsilon):
            print('f(x*) =', findFunctionValue(beta))
            print('x = %.20f' % beta)
            makeStep(alpha, 1)
    elif(findFunctionValue(alpha) < -epsilon):
        makeStep(beta, 0)
    elif(abs(findFunctionValue(alpha)) < epsilon):
        if(abs(findFunctionValue(beta)) < epsilon):
            print('x = %d' % ((alpha + beta) / 2))
            return
        print('f(x*) =', findFunctionValue(alpha))
        print('x = %.20f' % alpha)
        makeStep(beta, 0)

def findRoot(leftBorder, rightBorder, epsilon = e):
    value = (leftBorder + rightBorder) / 2
    
    
    while(abs(findFunctionValue(value)) > epsilon):
       
        if(findFunctionValue(leftBorder) * findFunctionValue(value) < 0):
            rightBorder = value
        elif(findFunctionValue(rightBorder) * findFunctionValue(value) < 0):
            leftBorder = value
            
        
        value = (leftBorder + rightBorder) / 2

    print('f(x*) =', findFunctionValue(value))
    print('x =', value)
    

def findFunctionValue(value, aCoef = a, bCoef = b, cCoef = c):
    result = (value ** 3) + aCoef * (value ** 2) + bCoef * value + cCoef
    
    return result

def makeStep(start, flag, delta = d):
    rightBorder = 0
    leftBorder = 0
    if(flag):
        rightBorder = start
        leftBorder = start - delta
        
        while(findFunctionValue(leftBorder) > 0):
            rightBorder = leftBorder
            leftBorder -= delta
        findRoot(leftBorder, rightBorder)
    
    else:
        leftBorder = start
        rightBorder = start + delta
        
        while(findFunctionValue(rightBorder) < 0):
            leftBorder = rightBorder
            rightBorder += delta
        findRoot(leftBorder, rightBorder)

def findRootWithStep(start, flag):
    if(flag):
        makeStep(start, flag)
    else:
        makeStep(start, flag)

def findRootSide(epsilon = e):
    if(abs(c) <= epsilon):
        print('f(x*) =',findFunctionValue(c))
        print('x = 0')
    elif(c > epsilon):
        findRootWithStep(0, 1)
    elif(c < -epsilon):
        findRootWithStep(0, 0)

if(discr <= 0):
    findRootSide()
else:
    findDiscRoots()
print(findFunctionValue(0))
