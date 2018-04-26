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
balance = 4213
monthlyPaymentRate = 0.04
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = 0
remainingBalance = 0

totalPayment = 0
monthlyInterestRate = annualInterestRate/12.0
for month in range(1,13):
    monthlyPayment = balance*monthlyPaymentRate    
    totalPayment+=monthlyPayment
    balance = (balance-monthlyPayment)*(1.0+monthlyInterestRate)
    print ("Month: " + str(month))
    print ("Minimum monthly payment: " + str(round(monthlyPayment,2)))
    print ("Remaining balance: " + str(round(balance,2)))
print("Total paid: "+str(round(totalPayment,2)))
print("Remaining balance: "+str(round(balance,2)))
