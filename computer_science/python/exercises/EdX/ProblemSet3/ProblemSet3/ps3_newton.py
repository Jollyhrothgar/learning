# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    polyPower = 0.0
    polyEval = 0.0
    for polyCoefficient in poly:
        polyEval += (x**polyPower)*polyCoefficient
        polyPower+=1
    return float(polyEval)




# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].

    In other words, we want the actual polynomial derivative, not the value
    of the derivative evaluated at a given point, x
    
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # Since we do not know ahead of time what polynomial is being
    # differentiated, we define a dynamic list.
    # FILL IN YOUR CODE HERE...
    if len(poly) == 1:
        return [0.0]
    else:
        polyDerivative = []
        for polyPower in range(1,len(poly)):
            polyDerivative.append(float(polyPower*poly[polyPower]))
        return polyDerivative




# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    # x_0 -> 0th iteration has been supplied.
    # A polynomial can have as many roots as it has non-zero powers

    # check if x_0 is close enough to the root (ie, value of function is zero)
    iterations = 0
    rootVal = evaluatePoly(poly,x_0) #f(x_0)
    rootDerivative = computeDeriv(poly) #f'(x)
    rootGuess = x_0
    while abs(rootVal) > epsilon:
        rootVal = evaluatePoly(poly,rootGuess) # f(x_n)
        rootDerivativeVal = evaluatePoly(rootDerivative, rootGuess) #f'(x_n)
        if abs(rootVal) < epsilon:
            return [float(rootGuess),int(iterations)]
            break
        else:
            # x_n+1 = x_n - f(x_n)/f'(x_n)
            rootGuess = rootGuess - rootVal/rootDerivativeVal
            iterations+=1
    return [float(rootGuess),int(iterations)]
            
## Main Program ##
print computeRoot([1, 9, 8], -3, .01)
