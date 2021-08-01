import sys
import math

# Global Variables Used For Debt Calculation
principal = 0
interest_rate = 0
payoff_time_months = 0
break_even_payment = 0
minimum_monthly_payment = 0
min_selection = 1
max_selection = 5
debt_parameters_defined = False

# Show menu for new debt calculation
def show_menu():
  print "===DEBT CALCULATOR MENU==="
  print "Choose an Option Below"
  print "\t [1] Input debt parameters"
  print "\t [2] Calculate months to pay off given payment amount"
  print "\t [3] Calculate break-even payment"
  print "\t [4] Calculate monthly payment given N-month payoff interval"
  print "\t [5] Quit"
  
# Define Debt Parmeters
def input_debt_params():
  """Enters a loop where user inputs debt parameters"""
  global principal
  global interest_rate
  global debt_parameters_defined
  doLoop = True
  print "Input Debt Parameters"
  while doLoop:
    try:
      principal = float(raw_input("\t Input Principal: "))
      if principal > 0:
        doLoop = False
      else:
        print "You entered a negative number. Try again"
    except ValueError:
      print "You entered a badly formated number. Try again."
  doLoop = True
  while doLoop:
    try:
      interest_rate = float(raw_input("\t Input yearly fractional interest rate ( example: 0.07 = 7% ): "))
      if interest_rate > 0:
        doLoop = False
        debt_parameters_defined = True
      else:
        print "Enter a positive interest rate. Try again"
    except ValueError:
      print "You entered a badly formatted number. Try again."
# Payoff Check
def payoff_check():
  global principal
  global interest_rate
  global payoff_time_months
  local_principal = principal
  local_interest_rate = interest_rate
  local_payoff_time = payoff_time_months
  total_paid = 0
  months = 0
  doLoop = True
  if debt_parameters_defined:
    while doLoop:
      try:
        payment = float(raw_input("\t Enter monthly payment amount: "))
        if payment > 0:
          doLoop = False
        else:
          print "Enter a positive monthly payment. Try again"
      except ValueError:
        print "You entered a badly formatted number. Try again."
    minimum_monthly_payment = (local_principal * local_interest_rate)/12.0
    if minimum_monthly_payment >= payment:
      delta = minimum_monthly_payment - payment
      if(delta < 0.1):
        print "\t\n You will only be able to pay your yearly interest"
      else:
        print "\t\n You are not paying enough. Your principal will increase by $", delta*12.0, " per year.\n"
    else:
      while local_principal > 0:
        total_paid+=payment
        if months%12 == 0:
          local_principal = local_principal*(1+local_interest_rate)
        local_principal = local_principal - payment
        months += 1
      print "\n\tWith your payment of $", payment, " per month, you will be debt free in ", months, " months (", round(months/12.0,2), " years)"
      print "\tYou must pay a total of $", total_paid, " which is actually ", round(total_paid/principal,2), "times the principal"
      print "\tEven with an interest rate of ", round(interest_rate*100,2), "%, you actually pay back the principal + ",round((100.0*(total_paid-principal)/principal),2) ,"% of the principal\n"
  else:
    print "You haven't intialized your debt paramters yet."

def getBalance(payment, interest, months, balance):
  '''
  Usage: getBalance(monthly payment, fractional yearly interest rate, number of months to pay off, starting balance)
  Returns: floating point number indicating the remaining balance
  Helper funciton for performing a bisection search to determine the ideal monthly payment to reduce debt to
  zero for a given number of months
  '''
  for n in range (0,months):
    balance = balance - payment
    if n%12 == 0:
      balance = balance*(1 + interest)
  return balance

# N-Month payoff
def n_month_payoff():
        global principal
        global interest_rate
        global debt_parameters_defined
        n_months = 0
    
        local_principal = principal
        local_interest_rate = interest_rate
        if debt_parameters_defined == False:
                print "\n Debt parameters are not defined.\n"
        else:
                doLoop = True
                while doLoop:
                        try:
                                n_months = int(raw_input("\t Enter number of months to pay off debt: "))
                                if n_months > 0:
                                        doLoop = False
                                else:
                                        print "Enter a positive number of months. Try again"
                        except ValueError:
                                print "You entered a badly formatted number. Try again."
        
                ### BISECTION SEARCH ROOT FINDING ###
                # Guess lower bound of payback range
                lowerBound = principal/n_months
                # Guess upper bound of payback range
                upperBound = principal*((1.0+interest_rate)**(n_months/12.0))/(n_months/12.0)
                low = 0
                mp = 0
                hi = 0
                iterations = 0
                endloopbal = 1
                monthlyPayment = lowerBound
                while endloopbal > 0.01:
                        monthlyPayment = (lowerBound+upperBound)/2.0
                        low = getBalance(lowerBound    , interest_rate, n_months, principal)
                        mp  = getBalance(monthlyPayment, interest_rate, n_months, principal)
                        hi  = getBalance(upperBound    , interest_rate, n_months, principal)
                        if( math.copysign(1,low) != math.copysign(1,mp)):
                                upperBound = monthlyPayment
                        elif( math.copysign(1,mp) != math.copysign(1,hi)):
                                lowerBound = monthlyPayment
                        else:
                                print("Algorithm Error, or, lucky guess.")
                                break
                        iterations+=1
                        endloopbal = abs(round(getBalance(monthlyPayment,interest_rate,n_months, principal),2))
                print "\n\tTo pay off your debt in ", n_months, " months (", round(n_months/12.0,2), " years), you need to pay about $", round(monthlyPayment,2), " per month"
                print "\tYou must pay a total of $", round(n_months*monthlyPayment,2), " which is actually ", round((n_months*monthlyPayment)/principal,2), "times the principal"
                print "\tEven with an interest rate of ", round(interest_rate*100,2), "%, you actually pay back the principal + ",round((100.0*((monthlyPayment*n_months)-principal)/principal),2) ,"% of the principal\n"
                
# Main program Loop
def main():
  global principal
  global interest_rate
  global payoff_time_months
  global break_even_payment
  global minimum_monthly_payment
  global debt_parameters_defined
  
  print "WELCOME TO DEBT CALCULATOR"
  runProgram = True
  menu_selection = 0
  while runProgram:
    show_menu()
    try:
      menu_selection = int(raw_input("\t\t->  "))
      if menu_selection < 0 or menu_selection > 6:
        print "Try again, asshole!"
        continue
    except ValueError:
      print "Try again, asshole!"
      continue
    if menu_selection == 1:
      input_debt_params()
      print "\n\t Now using a principal of : $", principal , " and interest rate of ", interest_rate*100, "% per year"
      print "\t Unpaid interest is recompounded yearly."
      print "\n"
    elif menu_selection == 2:
      payoff_check()
    elif menu_selection == 3:
      if debt_parameters_defined:
        print "\n\t If you pay $", principal*interest_rate/12.0, " each month (" ,principal*interest_rate," yearly ), you will break even\n"  
      else:
        print "\nDebt parameters are not defined.\n"
    elif menu_selection == 4:       
      n_month_payoff()
    elif menu_selection == 5:
      print "Goodbye"
      break
# Run program
main()
