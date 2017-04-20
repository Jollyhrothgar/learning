import sys
import math

# Global Variables Used For Debt Calculation
principal = 0 # this is the amount of the loan taken out
annual_percent_interest = 0 # this is the yearly interest rate
payoff_time = 0 # given the pay-off interval, how many pay-off intervals until the loan is paid off.
break_even_payment = 0 # how much to pay exactly the interest
minimum_payment = 0 # minimum payment per payment interval
min_selection = 1
max_selection = 5
debt_parameters_defined = False
time_interval = 1 # how many time-intervals in one year? I.e. use 12 for 12 months, 365 for days, etc.
compounding_interest_interval = 1 # how many time-intervals pass before interest in compounded?
payment_interval = 1 # how many time-intervals pass before a payment is made
payment_interval_name = "interval"
time_interval_name = "interval" # purely for console output. User can ignore it or enter something.
compounding_interest_interval_name = "interval" # name for the compounding interest interval
# We are interested in studying the compounding interest of loans. We arbitrarily choose to 
# examine loans based on an annual percent interest rate. However, because I want to deal with
# both student loans, and credit card loans, I leave it up to the user to correctly set up 
# the payment profile.


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
	global annual_percent_interest
	global debt_parameters_defined
	global time_interval
	global compounding_interest_interval
	global compounding_interest_interval_name
	global payment_interval
	global payment_interval_name
	global time_interval_name
	doLoop = True
	print "Input Debt Parameters"
	# Principal Input Loop
	while doLoop:
		try:
			principal = float(raw_input("\t Input Principal: "))
			if principal > 0:
				doLoop = False
			else:
				print "You entered a negative number. Try again"
		except ValueError:
			print "You entered a badly formatted number. Try again."
			doLoop = True
	# Interest Rate Input Loop
	doLoop = True
	while doLoop:
		try:
			annual_percent_interest = float(raw_input("\t Input yearly fractional interest rate ( example: 0.07 = 7% ):	"))
			if annual_percent_interest > 0:
				doLoop = False
			else:
				print "Enter a positive interest rate. Try again"
		except ValueError:
			print "You entered a badly formatted number. Try again."
			doLoop = True
	# Time Interval Input Loop
	doLoop = True
	while doLoop:
		try:
			time_interval = float(raw_input("\t How will the year be subdivided? (example: choose 365 for days, choose 12 for months, or choose an arbitrary interval):	"))
			if time_interval > 0:
				doLoop = False
				time_interval_name_temp = raw_input("\t What is the name of your time interval (i.e. Day, Month, Year, etc - you can pick, I won't check if it makes sense.):	")
				if time_interval_name_temp: 
					time_interval_name = time_interval_name_temp
			else:
				print "Enter a positive time interval. Try again."
		except ValueError:
			print "You entered a badly formatted number. Try again."
			doLoop = True
	# Compounding Interval Input Loop
	doLoop = True	
	while doLoop:
		try:
			coumpounding_interest_interval = float(raw_input("\t Input compounding interval ( example, your APR is "+str(annual_percent_interest)+" but interest is compounded over a subset of time intervals):	"))
			if compounding_interest_interval > 0:
				doLoop = False
				compounding_interest_interval_name_temp = raw_input("\t What is the name of your compounding interest interval (i.e. Day, Month, Year, etc - you can pick, I won't check if it makes sense.):	")
				if compounding_interest_interval_name_temp: 
					compounding_interest_interval_name = compounding_interest_interval_name_temp
			else:
				print "Enter a compounding interest interval. Try again"
		except ValueError:
			print "You entered a badly formatted number. Try again."
			doLoop = True
	# Payment Interval Input Loop
	doLoop = True
	while doLoop:
		try:
			payment_interval = float(raw_input("\t Input payment interval (i.e. if monthly interval, choose 1 for monthly payment. If daily interval with monthly payment, choose 30, etc):	"))
			if payment_interval > 0:
				doLoop = False
				payment_interval_name_temp = raw_input("\t What is the name of your payment interval (i.e. Day, Month, Year, etc - you can pick, I won't check if it makes sense.):	")
				if payment_interval_name_temp: 
					payment_interval_name = payment_interval_name_temp
			else:
				print "Enter a positive payment interval. Try again"
		except ValueError:
			print "You entered a badly formatted number. Try again."
			doLoop = True
	# If we get here, then all the input loops were successful
	debt_parameters_defined = True
	print "\n"
	print "Assuming that you have a principal debt of "+str(principal)+"."
	print "The year is subdivided into "+str(time_interval)+" "+time_interval_name+"s."
	print "The APR for the loan is: "+str(annual_percent_interest*100)+"% and interest is compounded every "+str(compounding_interest_interval)+" "+compounding_interest_interval_name+"."
	print "You say that you plan to make a payment every "+str(time_interval)+" "+payment_interval_name+"s."
		
# wp Payoff Check
def payoff_check():
	global principal
	global annual_percent_interest
	global compounding_interest_interval
	global payment_interval
	global payoff_time
	global time_interval
	global time_interval_name
	local_principal = principal
	local_interest_rate = annual_percent_interest/compounding_interest_interval
	local_payoff_time = payoff_time
	total_paid = 0
	local_time_interval = 0
	doLoop = True
	# Calculate the interest rate per payment interval
	# Start from the whole A = P*exp(r*t) formula. This expects and interval of years (t). However, we can convert to any arbitrary interval, if we are guaranteed
	local_interest_rate
	
	if debt_parameters_defined:
		while doLoop:
			try:
				payment = float(raw_input("\t Enter payment amount (to be applied every "+str(payment_interval)+" "+payment_interval_name+"s: "))
				if payment > 0:
					doLoop = False
				else:
					print "Enter a positive monthly payment. Try again"
			except ValueError:
				print "You entered a badly formatted number. Try again."
		minimum_payment = (local_principal * local_interest_rate)/payment_interval
		if minimum_payment >= payment:
			delta = minimum_payment - payment
			if(delta < 0.1):
				print "\t\n You will only be able to pay your yearly interest"
			else:
				print "\t\n You are not paying enough. Your principal will increase by $", delta*payment_interval, " per year.\n"
		else:
			while local_principal > 0:
				if local_time_interval%compounding_interest_interval == 0:
					local_principal = local_principal*(1+local_interest_rate)
				if local_time_interval%payment_interval:
					local_principal = local_principal - payment
					total_paid += payment
				local_time_interval += 1
			print "\n\tWith your payment of $", payment, " per ", payment_interval, " ", payment_interval_name, "s you will be debt free in ", local_time_interval, " ", time_interval_name, "s."
			print "\tYou must pay a total of $", total_paid, " which is actually ", round(total_paid/principal,2), "times the principal"
			print "\tEven with an APR of ", round(annual_percent_interest*100,2), "%, you actually pay back the principal + ",round((100.0*(total_paid-principal)/principal),2) ,"% of the principal\n"
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
	global annual_percent_interest
	global debt_parameters_defined
	n_months = 0
	
	local_principal = principal
	local_interest_rate = annual_percent_interest
	if debt_parameters_defined == False:
		print "\n Debt parameters are not defined.\n"
	else:
		doLoop = True
		while doLoop:
			try:
				in_months = int(raw_input("\t Enter number of months to pay off debt: "))
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
		upperBound = principal*((1.0+annual_percent_interest)**(n_months/12.0))/(n_months/12.0)
		low = 0
		mp = 0
		hi = 0
		iterations = 0
		endloopbal = 1
		monthlyPayment = lowerBound
		while endloopbal > 0.01:
			monthlyPayment = (lowerBound+upperBound)/2.0
			low = getBalance(lowerBound	, annual_percent_interest, n_months, principal)
			mp	= getBalance(monthlyPayment, annual_percent_interest, n_months, principal)
			hi	= getBalance(upperBound	, annual_percent_interest, n_months, principal)
			if( math.copysign(1,low) != math.copysign(1,mp)):
				upperBound = monthlyPayment
			elif( math.copysign(1,mp) != math.copysign(1,hi)):
				lowerBound = monthlyPayment
			else:
				print("Algorithm Error, or, lucky guess.")
				break
			iterations+=1
			endloopbal = abs(round(getBalance(monthlyPayment,annual_percent_interest,n_months, principal),2))
		print "\n\tTo pay off your debt in ", n_months, " months (", round(n_months/12.0,2), " years), you need to pay about $", round(monthlyPayment,2), " per month"
		print "\tYou must pay a total of $", round(n_months*monthlyPayment,2), " which is actually ", round((n_months*monthlyPayment)/principal,2), "times the principal"
		print "\tEven with an interest rate of ", round(annual_percent_interest*100,2), "%, you actually pay back the principal + ",round((100.0*((monthlyPayment*n_months)-principal)/principal),2) ,"% of the principal\n"
				
# Main program Loop
def main():
	global principal
	global annual_percent_interest
	global payoff_time
	global break_even_payment
	global minimum_payment
	global debt_parameters_defined
	
	print "WELCOME TO DEBT CALCULATOR"
	runProgram = True
	menu_selection = 0
	while runProgram:
		show_menu()
		try:
			menu_selection = int(raw_input("\t\t->	"))
			if menu_selection < 0 or menu_selection > 6:
				print "Try again, asshole!"
				continue
		except ValueError:
			print "Try again, asshole!"
			continue
		if menu_selection == 1:
			input_debt_params()
			print "\n\t Now using a principal of : $", principal , " and interest rate of ", annual_percent_interest*100, "% per year"
			print "\t Unpaid interest is recompounded yearly."
			print "\n"
		elif menu_selection == 2:
			payoff_check()
		elif menu_selection == 3:
			if debt_parameters_defined:
				print "\n\t If you pay $", principal*annual_percent_interest/12.0, " each month (" ,principal*interest_rate," yearly ), you will break even\n"	
			else:
				print "\nDebt parameters are not defined.\n"
		elif menu_selection == 4:			 
			n_month_payoff()
		elif menu_selection == 5:
			print "Goodbye"
			break
# Run program
main()
