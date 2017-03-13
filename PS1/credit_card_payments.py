# Problem Set 1
# Name: Aaron Bell
# Collaborators: John Doe
# Time Spent: 3:30 

# Problem 1
# Write a program to calculate the credit card balance after one year if a person only pays the
# minimum monthly payment required by the credit card company each month.
# Use raw_input() to ask for the following three floating point numbers:
# 1. the outstanding balance on the credit card
# 2. annual interest rate
# 3. minimum monthly payment rate
# For each month, print:
#	- the minimum monthly payment, 
#	- remaining balance, 
#	- principle paid in the
# format shown in the test cases below. All numbers should be rounded to the nearest penny.
# Finally, print the result, which should include the total amount paid that year and the remaining
# balance

# remaining_balance = float(input('What*s the current balance on the credit card: '))
# annual_interest_rate = float(input('What*s the APY of the card: '))
# minimum_monthly_payment_rate = float(input("What*s the minimum monthly payment rate: "))

def percentify(thing_to_percentify):
	if thing_to_percentify > 1: thing_to_percentify = thing_to_percentify / 100
	return thing_to_percentify
	
# annual_interest_rate = percentify(annual_interest_rate)
# print('The result of my percentify() for annual_interest_rate is: ' + str(annual_interest_rate))
# minimum_monthly_payment_rate = percentify(minimum_monthly_payment_rate)
# print ('The result of my percentify() for minimum_monthly_payment is: ' + str(minimum_monthly_payment_rate))


# total_paid_to_date = 0

# for month in range(0, 12):
	
	
	# minimum_monthly_payment = round((minimum_monthly_payment_rate * remaining_balance), 2)
	# interest_paid = round((annual_interest_rate / 12 * remaining_balance), 2)
	# principal_paid = round((minimum_monthly_payment - interest_paid), 2)
	# remaining_balance = round((remaining_balance - principal_paid), 2)
	
	# total_paid_to_date = round((total_paid_to_date + interest_paid), 2)
	
	# print('Month: ' + str(month + 1))
	# print('\n\nThe minimum monthly payment: $' + str(minimum_monthly_payment))
	# print('Interest paid: $' + str(interest_paid))
	# print('Principal paid: $' + str(principal_paid))
	# print('Remaining balance: $' + str(remaining_balance) )
	# print('Total amount paid to date: $' + str(total_paid_to_date))	

# print('\n\nRESULT\n\n' + 'Total amount paid: $' + str(total_paid_to_date) + '\nRemaining Balance: $' + str(remaining_balance))
	
# Paying Debt Off In a Year
# Problem 2 
	
# Now write a program that calculates the minimum fixed monthly payment needed in order pay
# off a credit card balance within 12 months. We will not be dealing with a minimum monthly
# payment rate.
# Take as raw_input() the following floating point numbers:
# 	1. the outstanding balance on the credit card
# 	2. annual interest rate as a decimal 
# Print out:
#	the fixed minimum monthly payment, 
#	number of months (at most 12 and possibly less than 12) it takes to pay off the debt, and 
#	the balance (likely to be a negative number).
# Assume that the interest is compounded monthly according to the balance at the start of the
# month (before the payment for that month is made). The monthly payment must be a multiple of
# $10 and is the same for all months. Notice that it is possible for the balance to become negative
# using this payment scheme. In short:
# Monthly interest rate = Annual interest rate / 12.0
# Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum
# monthly payment 

# Where I learned to do bisectional search:



# APY = percentify(float(input('GIVE ME YOUR APY: ')))
# starting_balance = int(input('Enter your balance: '))
# remaining_balance = starting_balance
# months_to_a_clear_balance = int(input('How many months from now do you want this balance cleared: '))

# epsilon = 100 # approximation factor
# numGuesses = 0
# low = 0
# high = int(remaining_balance)
# current_payment = round((high + low)/2.0, -1)

# # Have it go through the APY process... applying the current guess as the payment for each month--and see if the balance at the end of 12 months = 0 +- epsilon

# while abs(remaining_balance) >= epsilon:

	# print('\nlow: ' + str(low) + 'high: ' + str(high) + 'current_payment: ' + str(current_payment) + '\n')
	
	# numGuesses += 1
	
	# remaining_balance = starting_balance
	
	# print('$' + str(starting_balance))
	
	# for month in range(0, months_to_a_clear_balance):
		
		# remaining_balance = remaining_balance * (1 + (APY / months_to_a_clear_balance)) - current_payment
		
		# print('Remaining balance after payment on month ' + str(month + 1) + ': ' + str(remaining_balance) + '')
		
	# print('\nRemaining balance after ' + str(months_to_a_clear_balance) + ' months of paying $ ' + str(current_payment) + ' every month: ' + str(remaining_balance) + '\n') 
		
	# if remaining_balance > epsilon:
	
		# low = current_payment
		
	# elif remaining_balance < epsilon:
	
		# high = current_payment
		
	# current_payment = round((high + low)/2.0, -1)

	
# while remaining_balance > 0:
	
	# print('current_payment before: ' + str(current_payment))
	
	# current_payment += 10 # Because the code randomly takes of 10 after the while loop, and I don't know why
	
	# print('current_payment after: ' + str(current_payment))

	# remaining_balance = starting_balance

	# for month in range(0, months_to_a_clear_balance):
		
		# remaining_balance = remaining_balance * (1 + (APY / months_to_a_clear_balance)) - current_payment
		
		# print('Remaining balance after payment on month ' + str(month) + ': ' + str(remaining_balance) + '')

	# print('\nRemaining balance after ' + str(months_to_a_clear_balance) + ' months of paying $' + str(current_payment) + ' every month: ' + str(remaining_balance)) 		
	
	# print('numGuesses =', str(numGuesses))
	
	# print(str(current_payment), 'will pay off $', str(starting_balance), ' in ' + str(months_to_a_clear_balance) + ' months.')

# for month in range(0,12):
	# print('Month: ' + str(month))
	# remaining_balance = remaining_balance * (1 + (APY / 12))
	# current_payment = remaining_balance / (12 - month)
	# print('Current Payment: $' + str(current_payment))
	# remaining_balance = remaining_balance - current_payment
	# print('Remaining Balance: $' +  str(remaining_balance))
	
	

# # # # # # # # # # # # # # # # # # # # 

# Modified Upper And Lower Bounds

# # # # # # # # # # # # # # # # # # # # 

# Monthly payment lower bound = Balance / 12.0
# Monthly payment upper bound = (Balance * (1 + (Annual interest rate / 12.0)) ** 12.0) / 12.0

# APY = percentify(float(input('GIVE ME YOUR APY: ')))
# starting_balance = int(input('Enter your balance: '))
# remaining_balance = starting_balance
# months_to_a_clear_balance = int(input('How many months from now do you want this balance cleared: '))

# epsilon = 100 # approximation factor
# numGuesses = 0
# low = remaining_balance / 12.0
# high = (remaining_balance * (1 + (APY /12.0)) ** 12.0) / 12.0
# current_payment = round((high + low)/2.0, -1)

# # Have it go through the APY process... applying the current guess as the payment for each month--and see if the balance at the end of 12 months = 0 +- epsilon

# while abs(remaining_balance) >= epsilon:

	# print('\nlow: ' + str(low) + 'high: ' + str(high) + 'current_payment: ' + str(current_payment) + '\n')
	
	# numGuesses += 1
	
	# remaining_balance = starting_balance
	
	# print('$' + str(starting_balance))
	
	# for month in range(0, months_to_a_clear_balance):
		
		# remaining_balance = remaining_balance * (1 + (APY / months_to_a_clear_balance)) - current_payment
		
		# print('Remaining balance after payment on month ' + str(month + 1) + ': ' + str(remaining_balance) + '')
		
	# print('\nRemaining balance after ' + str(months_to_a_clear_balance) + ' months of paying $ ' + str(current_payment) + ' every month: ' + str(remaining_balance) + '\n') 
		
	# if remaining_balance > epsilon:
	
		# low = current_payment
		
	# elif remaining_balance < epsilon:
	
		# high = current_payment
		
	# current_payment = round((high + low)/2.0, -1)

	
# while remaining_balance > 0:
	
	# print('current_payment before: ' + str(current_payment))
	
	# current_payment += 10 # Because the code randomly takes of 10 after the while loop, and I don't know why
	
	# print('current_payment after: ' + str(current_payment))

	# remaining_balance = starting_balance

	# for month in range(0, months_to_a_clear_balance):
		
		# remaining_balance = remaining_balance * (1 + (APY / months_to_a_clear_balance)) - current_payment
		
		# print('Remaining balance after payment on month ' + str(month) + ': ' + str(remaining_balance) + '')

	# print('\nRemaining balance after ' + str(months_to_a_clear_balance) + ' months of paying $' + str(current_payment) + ' every month: ' + str(remaining_balance)) 		
	
	# print('numGuesses =', str(numGuesses))
	
	# print(str(current_payment), 'will pay off $', str(starting_balance), ' in ' + str(months_to_a_clear_balance) + ' months.')


# # # # # # # # # # # # # # # # # # # # 

# Modified Upper And Lower Bounds

# # # # # # # # # # # # # # # # # # # # 

# Monthly payment lower bound = Balance / 12.0
# Monthly payment upper bound = (Balance * (1 + (Annual interest rate / 12.0)) ** 12.0) / 12.0

#[klIMPROVE: Loop the answer until the condition is an int or float]



try: 
	APY = percentify(float(input('GIVE ME YOUR APY: ')))
except ValueError:
	
	def apy_except_handler():

		try: 
		
			APY = float(input('Please enter a number for your APY'))
			return APY
			
		except ValueError: 
		
			APY = apy_except_handler()
			return APY
	
	APY = percentify(apy_except_handler())
		
print('Pre-percentified APY: ' + str(APY))

starting_balance = int(input('Enter your balance: '))
remaining_balance = starting_balance
months_to_a_clear_balance = int(input('How many months do you want this balance paid off in: '))

epsilon = 1 # approximation factor
numGuesses = 0
low = remaining_balance / float(months_to_a_clear_balance)
high = (remaining_balance * ((1 + (APY /12.0)) ** months_to_a_clear_balance) / months_to_a_clear_balance)
current_payment = round(((high + low)/2.0), 2)

print('WHERE X IS THIS Rounded current payment: ' + str(current_payment))

# Have it go through the APY process... applying the current guess as the payment for each month--and see if the balance at the end of 12 months = 0 +- epsilon

while abs(remaining_balance) >= epsilon:

	print('\nlow: ' + str(low) + 'high: ' + str(high) + 'current_payment: ' + str(current_payment) + '\n')
	
	numGuesses += 1
	print(numGuesses)
	
	remaining_balance = starting_balance
	
	print('$' + str(starting_balance))
	
	for month in range(0, months_to_a_clear_balance):
		
		remaining_balance = remaining_balance * (1 + (APY / 12)) - current_payment
		
		print('Remaining balance after payment on month ' + str(month + 1) + ': ' + str(remaining_balance) + '')
		
	print('\nRemaining balance after ' + str(months_to_a_clear_balance) + ' months of paying $ ' + str(current_payment) + ' every month: ' + str(remaining_balance) + '\n') 
		
	if remaining_balance > epsilon:
	
		low = current_payment
		
	elif remaining_balance < epsilon:
	
		high = current_payment
		
	current_payment = round(((high + low)/2.0), 2)
	print('WHERE Y IS THIS Rounded new current payment: ' + str(current_payment))

numNewGuesses = 0 
	
while remaining_balance > 0:	
	
	print('current_payment before: ' + str(current_payment))
	
	current_payment += .01 # Because the code randomly takes of 10 after the while loop, and I don't know why
	
	numNewGuesses += 1
	print('Fine-tuned {} number of times.'.format(str(numNewGuesses)))
	
	print('current_payment after: ' + str(current_payment))

	remaining_balance = starting_balance

	for month in range(0, months_to_a_clear_balance):
		
		remaining_balance = remaining_balance * (1 + (APY / months_to_a_clear_balance)) - current_payment
		
		print('Remaining balance after payment on month ' + str(month) + ': ' + str(remaining_balance) + '')

	print('\nRemaining balance after ' + str(months_to_a_clear_balance) + ' months of paying $' + str(current_payment) + ' every month: ' + str(round(remaining_balance, 2)))		
	
	print('numGuesses =', str(numGuesses))
	
	print(str(current_payment), 'will pay off $', str(starting_balance), ' in ' + str(months_to_a_clear_balance) + ' months.')