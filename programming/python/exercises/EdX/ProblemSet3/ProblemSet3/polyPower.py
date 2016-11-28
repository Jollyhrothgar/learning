# Polynomial Lists #
# In this program, we represent coefficients of polynomials as lists.
# The list index corresponds to the polynomial term power (ie, list[0] holds
# the coeffient for x**0, and so-on.

## Evaluate a Function ##
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
## Take a derivative of a function ##
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

## Main Program ##
print evaluatePoly([0.0, 0.0, 5.0, 9.3, 7.0], -13)
print computeDeriv([4, 0, 8, 1])
