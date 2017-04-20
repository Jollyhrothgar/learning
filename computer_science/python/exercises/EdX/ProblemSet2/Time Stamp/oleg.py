import time

balance = 987654321
startingBalance = balance
annualInterestRate = 0.02
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12
TotalPaid = 0.00
LowerBound = balance / 12
UpperBound = (balance * (1+monthlyInterestRate)**12)/12
#print FixedPayment

def Balance(PrevBalance, MonthlyPayment, Interest):
    currentBalance = (PrevBalance - MonthlyPayment)*(1.00 + Interest)
    return currentBalance

def minPayment(X):
    minPayment = X * monthlyPaymentRate
    return minPayment

def guess(a, b):
    midPoint = (a + b) / 2
    return midPoint

def endingBalance(balance, monthlyInterestRate):
    i = 1
    while (i <= 12):
        #payment = 
        balance = Balance(balance, guess(LowerBound, UpperBound), monthlyInterestRate)
        i = i + 1
    return balance

while (abs(startingBalance) > 0.001):
    startingBalance = balance
    FixedPayment = guess(LowerBound, UpperBound)
    startingBalance = endingBalance(startingBalance, monthlyInterestRate)
    #print startingBalance
    if (startingBalance <  0):
        UpperBound = guess(LowerBound, UpperBound)
        #print ("UpperBound is: " + str(UpperBound))
    else:
        LowerBound = guess(LowerBound, UpperBound)
        #print ("lowerbound is: " + str(LowerBound))
    
print ("Lowest Payment is: " + str(round(FixedPayment, 2)))
print ("Time: " + str(time.clock()))
#endingBalance(balance, monthlyInterestRate)
