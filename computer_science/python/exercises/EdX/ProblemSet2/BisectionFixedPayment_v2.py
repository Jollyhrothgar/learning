# Continuous search (increments of 0.01) to find minimum monthly payment
# using bisecting search
#
# Goal is to find minumum constant monthly payment to pay off a loan in
# 12 months.
#

## Modules ##
import math

## Test Values ##
balance = 320000
annualInterestRate = 0.2

## Pasted Program Submission ##

### Global Variables ###
monthlyInterestRate = annualInterestRate/12.0
iterations = 0

def getBalance(payment,interest,balance):
    '''
    Usage: (monthly payment, monthly interest, one-year balance)
    returns a floating point number, which is balance
    '''
    for n in range(0,12):
        balance = (balance-payment)*(1.0+interest)
    return balance

# Underestimate
lowerBound = balance/12.0
# Overestimate
upperBound = balance*((1.0+monthlyInterestRate)**12)/12.0
low = 0
mp = 0
hi = 0
endloopbal = 1
monthlyPayment = lowerBound
#print("Principal: "+str(balance))
while endloopbal > 0.01:
    # Calculate amount payed, find remaining balance
    monthlyPayment = (lowerBound+upperBound)/2.0

    # Calculate 'functional value' of each monthly payment
    low = getBalance(lowerBound,monthlyInterestRate,balance)
    mp  = getBalance(monthlyPayment,monthlyInterestRate,balance)
    hi  = getBalance(upperBound,monthlyInterestRate,balance)

    ##BISECTION ROOT FINDING##
    
    # If the balance of the low-guess and mid-point guess have opposite signs,
    # Then the current midpoint is guaranteed to lie below the root (in y). 
    if( math.copysign(1,low) != math.copysign(1,mp)):
        upperBound = monthlyPayment
    # If the balance of the mid-point guess and the high-guess have opposite signs,
    # Then the current midpoint is guaranteed to lie above the root (in y)
    elif( math.copysign(1,mp) != math.copysign(1,hi)):
        lowerBound = monthlyPayment
    # We only get here in the unlikely case that we guessed the midpoint
    else:
        print("Algorithm Error, or, lucky guess.")
        break
    iterations+=1

    # We can terminate the loop once our balance has reached arbitrarily close
    # to the real balance (via testing that the end-of-year balance using our monthly
    # payment is a very small number)
    endloopbal = abs(round(getBalance(monthlyPayment,monthlyInterestRate,balance),2))
print("Lowest Payment: " + str(round(monthlyPayment,2)))
#print("Number of iterations: " +str(iterations))
