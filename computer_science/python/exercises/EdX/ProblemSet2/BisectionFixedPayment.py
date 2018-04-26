# This program uses the bisection search to find the minimum monthly payment one must pay
# to pay off a debt in one year, where debt is continuously compounding
# Note that:
#   Monthly Interest Rate = (annual interest rate) / 12
#   Minumum monthly payment = (Minimum monthly payment rate)*(Previous Balance)
#   Updated balance each month = (Previous balance - minimum monthly payment)*(1+Monthylu interest rate)
#

# Test Values
balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
remainingBalance = 0

# Using exhaustive iteration
totalPayment = 0
monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = 0
originalBalance = balance
iterations = 0
lowerBound = balance/12.0
upperBound = balance*((1.0+monthlyInterestRate)**12)/12.0
monthlyPayment = lowerBound
while balance > 0.0:
    balance = originalBalance
    totalPayment = 0
    for month in range(1,13):    
        totalPayment+=monthlyPayment
        balance = (balance-monthlyPayment)*(1.0+monthlyInterestRate)
        print("\tMonth: "+str(month))
        print("\tTotal paid: "+str(round(totalPayment,2)))
        print("\tRemaining balance: "+str(round(balance,2)))
        if(balance < 0.0):
            break
        
    print("Yearly Total paid: "+str(round(totalPayment,2)))
    print("Yearly Remaining balance: "+str(round(balance,2)))
    # Bisection Happens here
    if(balance > 0.0):
        lowerBound += (upperBound-lowerBound)/2
        monthlyPayment = lowerBound
    iterations+=1
print ("Lowest Payment: "+str(monthlyPayment))
print ("Iterations: " + str(iterations))
