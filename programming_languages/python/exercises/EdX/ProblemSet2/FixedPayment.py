#
# This program solves the compund interest problem, assuming that the user assigns
# values for three parameters:
#   balance -> outstanding balance on credit card
#   annualInterestRate -> annualinterest rate as decimal value
#   monthlyPaymentRate -> minimum monthly payment rate, as a decimal
#
#
# Note that:
#   Monthly Interest Rate = (annual interest rate) / 12
#   Minumum monthly payment = (Minimum monthly payment rate)*(Previous Balance)
#   Updated balance each month = (Previous balance - minimum monthly payment)*(1+Monthylu interest rate)
#

# Test Values
balance = 4773
monthlyPaymentRate = 0.04
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
remainingBalance = 0

#Submission
def getBalance(payment,interest,balance):
    '''
    Usage: (monthly payment, monthly interest, one-year balance)
    returns a floating point number, which is balance
    '''
    for n in range(0,12):
        balance = (balance-payment)*(1.0+interest)
    return balance

# Using exhaustive iteration

totalPayment = 0
monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = 0
originalBalance = balance
iterations = 0
while balance > 0.0:
    balance = originalBalance
    totalPayment = 0
    balance = getBalance(monthlyPayment,monthlyInterestRate,balance)
    #for month in range(1,13):    
    #    totalPayment+=monthlyPayment
    #   balance = (balance-monthlyPayment)*(1.0+monthlyInterestRate)
    #print("Total paid: "+str(round(totalPayment,2)))
    #print("Remaining balance: "+str(round(balance,2)))
    if(balance > 0.0):
        monthlyPayment+=10
    iterations+=1
print ("Lowest Payment: "+str(monthlyPayment))
#print ("Iterations: " + str(iterations))
