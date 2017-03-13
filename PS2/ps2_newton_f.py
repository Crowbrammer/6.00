# Problem Set 2
# Name: Aaron Bell
# Collaborators (Discussion): John Doe
# Collaborators (Identical Solution): Jane Smith
# Time: 

# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
	"""
	Computes the polynomial function for a given value x. Returns that value.

	Example:
	>>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
	>>> x = -13
	>>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
	180339.9

	poly: tuple of numbers, length > 0
	x: number
	returns: float
	"""
	# TO DO ... 

	#f = [f+= poly[a]*x**a for a in range(poly)]
	
	# f = 0
	
	# for a in range(poly):
		# f +=  poly[a]*x**a
	# return f
	
# poly = (0.0, 0.0, 5,0, 9.3, 7.0)
# x = -13
# print(evaluate_poly(poly, x))

# 1. Looks good so far. But I got: TypeError: 'tuple' object cannot be interpreted as an integer. Let's see if wrapping a len function will return the integer we need. 
	
	# f = 0
	
	# for a in range(len(poly)):
	
		# f +=  poly[a]*x**a
		
	# return f
	
# poly = (0.0, 0.0, 5,0, 9.3, 7.0)
# x = -13
# print('evaluate_poly(poly, x): 'evaluate_poly(poly, x))

# 2. This worked. Printed out '-2332588.7'. Testing it with a hardcoded expression.

	# f = 0
	
	# for a in range(len(poly)):
	
		# f +=  poly[a]*x**a
		
	# return f
	
# poly = (0.0, 0.0, 5,0, 9.3, 7.0)
# x = -13
# print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))

# print('f(-13) = 5.0(-13)**2 + 9.3(-13)**3 + 7.0(13)**4: ' + str(5.0(-13)**2 + 9.3(-13)**3 + 7.0(13)**4))

# 3. This didn't work. TypeError: float object not callable. Need to add multiplication operators after the parentheses in the expression. 

	# f = 0
	
	# for a in range(len(poly)):
		# f +=  poly[a]*x**a
		
	# return f
	
# poly = (0.0, 0.0, 5,0, 9.3, 7.0)
# x = -13
# print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))

# print('f(-13) = 5.0(-13)**2 + 9.3(-13)**3 + 7.0(13)**4: ' + str(5.0*(-13)**2 + 9.3*(-13)**3 + 7.0*(13)**4 ))

# 4. Worked, but semantically incorrect. The value I* got differed from the one originally provided (Which, btw, was negative, versus my new positive one.). Figure out what's up.

	# f = 0
	
	# for a in range(len(poly)):
		# print('a: ' + str(a), 'poly: ' + str(poly), 'poly[a]: ' + str(poly[a]))
		# f +=  poly[a]*x**a
		
		# print('f: ' + str(f))
		
	# return f
	
# poly = (0.0, 0.0, 5,0, 9.3, 7.0)
# x = -13
# print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))

# print('f(-13) = 5.0(-13)**2 + 9.3(-13)**3 + 7.0(13)**4: ' + str(5.0*(-13)**2 + 9.3*(-13)**3 + 7.0*(13)**4 ))

# 5. Print statements don't show's evaluated each time. Change that. 


	# f = 0
	
	# for a in range(len(poly)):
		# print('\na: ' + str(a), 'poly: ' + str(poly), 'poly[a]: ' + str(poly[a]))
		
		# f +=  poly[a]*x**a
		
		# print('{}*{}**{}:'.format(str(poly[a]), str(x), str(a)))
		# print('f: ' + str(f))
		
	# return f
	
# poly = (0.0, 0.0, 5,0, 9.3, 7.0)
# x = -13
# print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))

# print('f(-13) = 5.0(-13)**2 + 9.3(-13)**3 + 7.0(13)**4: ' + str(5.0*(-13)**2 + 9.3*(-13)**3 + 7.0*(13)**4 ))

# 6. The function is skipping over the 3rd poly for some reason. Find I a way to correct this.

	# f = 0
	
	# for a in range(len(poly)):
		# print('\na: ' + str(a), 'poly: ' + str(poly), 'poly[a]: ' + str(poly[a]))
		
		# f +=  poly[a]*x**a
		
		
		# print('{}*{}**{}:'.format(str(poly[a]), str(x), str(a)))
		# print('f: ' + str(f))
		
	# return f
	
# poly = (0.0, 0.0, 5, 0, 9.3, 7.0)
# x = -13
# print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))

# print('f(-13) = 5.0(-13)**2 + 9.3(-13)**4 + 7.0(13)**5: ' + str(5.0*(-13)**2 + 9.3*(-13)**4 + 7.0*(-13)**5))

# 7. The function was correct in the first place. I mistook the comma for a period in the 3rd value of poly. Removing scaffolding. 

	# f = 0
	
	# try: 
	
		# for a in range(len(poly)):
			
			# try: 
			
				# f +=  poly[a]*x**a
				# print(str(all(isinstance(x, int) for x in f)) + ' at Line 156')
			
			# except TypeError: 
			
				# pass
				# print(str(all(isinstance(x, int) for x in f)) + ' at Line 161')
		
	# except TypeError:
	
		# f = (poly,)
		# print(str(all(isinstance(x, int) for x in f)) + ' at Line 166')
	
	
	# print(str(all(isinstance(x, int) for x in f)) + ' at Line 169') 
	# if all(isinstance(x, int) for x in f): 
	
		# return f
		
	# else:
	
		# return "There's a bogey (string or something) in the tuple."
	
# poly = 'Steve'
# x = 2

# print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))
# print('f(0.8067885094814566) = 5.0(0.8067885094814566)**2 + 9.3(0.8067885094814566)**4 + 7.0(0.8067885094814566)**5: ' + str((5.0*(x)**2 + 9.3*(x)**4 + 7.0*(x)**5)))

# 8. Kept getting excepted TypeErrors or 'non-iterables'. Can jam a tuple into an int object they say. 

	# f = (0.0,)
	
	# try: 
	
		# for a in range(len(poly)):
			
			# try: 
			
				# f +=  (poly[a]*x**a,)
			
			# except TypeError: 
			
				# print('str(checker(f)) isn*t working')
		
	# except TypeError:
	
		# f = (poly,)
	
	# # Check if there's something 'not right' in the tuple. 
	
	# if checker(f): 
	
		# return f
		
	# else:
	
		# return "There's a bogey in the tuple."

# 9. Forgot the original intent of the code. It needs to evaluate it, not create polynomial. 

	f = 0.0
	
	if checker(poly): 
	
		f = sum([poly[a]*x**a for a in range(len(poly))])
		return f
		
	else:
	
		return "There's a bogey in the tuple."
	
# DRY the code wit a checker function. Makes sure everything is of a float type. 
	
def checker(checkee, t=float, i=int):
	
	return all(isinstance(x, (t, i)) for x in checkee)
	

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x = 6

print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))
print('x**4 + 3x**3, + 17.5x**2 -13.39 == ' + str((x**4 + 3*x**3 + 17.5*x**2 -13.39)))

# 10. Replaced the for loop with the sum of a list comprehension. Removing about 5 lines of code, and making it more readable. 


# What the code represents. Also a test to compare the code's answer to. 

# def calc_med_dosage(hours):
	
	# c = (2, 2, -0.05)
	# return evaluate_poly(c, hours)

# # Not sure how this works, because it doesn't consider initial dose... but that's what they say to calculate.

# def rollercoaster_graph(x):
	
	# c = (2000, 976, 356, 200, 14, 0.14, -0.05)
	# return evaluate_poly(c, x)

# # I guess they just want it to look like a rollercoaster.
	
# #def motion_under_grav(x):
	
	# # c = ()
	
# Works (X)
# Robust (X)
# Better Than Expected (X)
# Understood () 


def compute_deriv(poly):
	"""
	Computes and returns the derivative of a polynomial function. If the
	derivative is 0, returns (0.0,).

	Example:
	>>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
	>>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
	(0.0, 35.0, 9.0, 4.0)

	poly: tuple of numbers, length > 0
	returns: tuple of numbers
	"""
	# TO DO ... 
	
	# Forgot to track iterations!
	
	# Bind the name 'f' to an empty tuple. 
	
	
	f = ()
			
	for a in range(len(poly)): # (0, 1, 2, 3, 4)
		
		# Reassign f to new tuple consisting of the original tuple, plus the value of the current index times the index (the constant times what was its power, for the power rule). 
		
		if a != 0:
			f = f + (poly[a]*a,)
		
	return f
	
'''

Before: f == ()
1: f == (0.0,)
2: f == (0.0, 0.0, )
3: f == (0.0, 0.0, 17.5*(2-1)

'''
	
# print('compute_deriv(poly): ' + str(compute_deriv(poly)))
# print("f'(x)  if f(x) == x^4 + 3x^3 + 17.5x^2 - 13.39: " + str(compute_deriv(poly)))

# Works ()
# Robust ()
# Better Than Expect ()
# Understood () 

def f(poly, x):

	return evaluate_poly(poly, x)
	
def f_deriv(poly):

	return compute_deriv(poly)

def compute_root(poly, x_0, epsilon):
	"""
	Uses Newton's method to find and return a root of a polynomial function.
	Returns a tuple containing the root and the number of iterations required
	to get to the root.

	Example:
	>>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
	>>> x_0 = 0.1
	>>> epsilon = .0001
	>>> print comput
	e_root(poly, x_0, epsilon)
	(0.80679075379635201, 8.0)

	poly: tuple of numbers, length > 1.
		 Represents a polynomial function containing at least one real root.
		 The derivative of this polynomial function at x_0 is not 0.
	x_0: float
	epsilon: float > 0
	returns: tuple (float, int)
	"""
	# TO DO ... 
	
	'''
	
	Newton’s method (also known as the Newton-Raphson method) is a successive approximation
	method for finding the roots of a function. Recall that the roots of a function f(x) are the values
	of x such that f(x) = 0. You can read more about Newton’s method here.
	Here is how Newton’s method works: 
	1.	 We guess some x0.
	2.	 We check to see if it’s a root or close enough to a root by calculating f(x0). If f(x0) is
	within some small value epsilon of 0, we say that’s good enough and call x0 a root.
	3.	 If f(x0) is not good enough, we need to come up with a better guess, x1. x1 is calculated
	by the equation: x1 = x0 - f(x0)/f'(x0).
	4.	 We check to see if x1 is close enough to a root. If it is not, we make a better guess x2 and
	check that. And so on and so on. For every xn that is not close enough to a root, we
	replace it with xn+1 = xn - f(xn)/f'(xn) and check if that’s close enough to a root. We
	repeat until we finally find a value close to a root.
	For simplicity, we will only be using polynomial functions in this problem set. 
	'''
	
	# x = [x_0]
	# numGuesses = 0
	
	# while f(poly, x) > epsilon or f(poly, x) < 0:
		
		# numGuesses += 1
		
		# x[numGuesses:numGuesses] = x[numGuesses -1] - f(poly, x[numGuesses -1])/f(f_deriv(x0), x[numGuesses -1])
	
	# return x, numGuesses
	
	# print('x{} ({}) is close enough to the root'.format(str(numGuesses), str(x)))
	# print('numGuesses: {}'.format(str(numGuesses)))

	# 1. 'TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int''. For the while conditional, I* passed the entire list for x, instead of its values. Now passing the values into it instead of the list.
	
	# x = [x_0]
	# numGuesses = 0
	
	# while f(poly, x[numGuesses]) > epsilon or f(poly, x[numGuesses]) < 0:
		
		# numGuesses += 1
		
		# x[numGuesses:numGuesses] = x[numGuesses -1] - f(poly, x[numGuesses -1])/f(f_deriv(x0), x[numGuesses -1])
	
	# return x, numGuesses
	
	# print('x{} ({}) is close enough to the root'.format(str(numGuesses), str(x)))
	# print('numGuesses: {}'.format(str(numGuesses)))
	
	# 2. 'NameError: name 'x0' is not defined'. Tried to pass an unknown varaible x0 into f_deriv, instead of the polynomial. Now passing the polynomial into instead of the list. 
	
	# x = [x_0]
	# numGuesses = 0
	
	# while f(poly, x[numGuesses]) > epsilon or f(poly, x[numGuesses]) < 0:
		
		# numGuesses += 1
		
		# x[numGuesses:numGuesses] = x[numGuesses -1] - f(poly, x[numGuesses -1])/f(f_deriv(poly), x[numGuesses -1])
	
	# return x, numGuesses
	
	# print('x{} ({}) is close enough to the root'.format(str(numGuesses), str(x)))
	# print('numGuesses: {}'.format(str(numGuesses)))
	
	# 3. 'ZeroDivisionError: float division by zero'. Changed x0 from 0 to 3. Need a way to make it robust from zero-division. 
	
	# x = [x_0]
	# numGuesses = 0
	
	# while f(poly, x[numGuesses]) > epsilon or f(poly, x[numGuesses]) < 0:
		
		# numGuesses += 1
		
		# x[numGuesses:numGuesses] = x[numGuesses -1] - f(poly, x[numGuesses -1])/f(f_deriv(poly), x[numGuesses -1])
	
	# return x, numGuesses
	
	# print('x{} ({}) is close enough to the root'.format(str(numGuesses), str(x)))
	# print('numGuesses: {}'.format(str(numGuesses)))
	
	# 4. 'TypeError: can only assign an iterable. Line 309. Going to print out the result, and try assigning the object a name.
	
	# x = [x_0]
	# numGuesses = 0
	
	# while f(poly, x[numGuesses]) > epsilon or f(poly, x[numGuesses]) < 0:
		
		# numGuesses += 1
		
		# # x[numGuesses:numGuesses] = x[numGuesses -1] - f(poly, x[numGuesses -1])/f(f_deriv(poly), x[numGuesses -1])
		# print(x[numGuesses -1] - f(poly, x[numGuesses -1])/f(f_deriv(poly), x[numGuesses -1]))
	
	# return x, numGuesses
	
	# print('x{} ({}) is close enough to the root'.format(str(numGuesses), str(x)))
	# print('numGuesses: {}'.format(str(numGuesses)))
	
	# 5. 'IndexError: list index out of range'. x[0] should == 3. Not sure 
	
	# x = [x_0]
	# numGuesses = 0
	
	# print('x[NumGuesses]: {}'.format(str(x[numGuesses])))
	
	# while f(poly, x[len(x) - 1]) > epsilon or f(poly, x[len(x) - 1]) < 0:
		
		# print('numGuesses: {}'.format(str(numGuesses)))
		# numGuesses += 1
		
		# # x[numGuesses:numGuesses] = x[numGuesses -1] - f(poly, x[numGuesses -1])/f(f_deriv(poly), x[numGuesses -1])
		# print(x[numGuesses -1] - f(poly, x[numGuesses -1])/f(f_deriv(poly), x[numGuesses -1]))
	
	# return x, numGuesses
	
	# print('x{} ({}) is close enough to the root'.format(str(numGuesses), str(x)))
	# print('numGuesses: {}'.format(str(numGuesses)))
	
	# 6. 'IndexError: list index out of range' Now for the print part on line 346. Going to try the way the problem set suggests. 
	
	# x = [x_0]
	# numGuesses = 0
	# x_l = len(x)
	
	# while abs(f(poly, x[len(x) - 1])) > epsilon:
		
		# numGuesses += 1
		# print('x[len(x) - 1]: ' + str(x[len(x) - 1]))
		# print('x == ' + str(x))
		# print('f(poly, x[len(x) - 1]): ' + str(f(poly, x[len(x) - 1])))
		# print('f_deriv(poly): ' + str(f_deriv(poly)))
		# print('f(f_deriv(poly), x[len(x) - 1]): ' + str(f(f_deriv(poly), x[len(x) - 1])))
		# print('{} - {} / {} == {}'.format(str(x[len(x) - 1]), str(f(poly, x[len(x) - 2])), str(f(f_deriv(poly), x[len(x) - 1])), str(x[len(x) - 1] - f(poly, x[len(x) - 1])/f(f_deriv(poly), x[len(x) - 1]))))
		
		# x.append(x[len(x) - 2] - f(poly, x[len(x) - 2])/f(f_deriv(poly), x[len(x) - 2]))
		# print(x[len(x) - 1:len(x) - 1])
		
	# print('x{} ({}) is close enough to the root'.format(str(len(x) - 1), str(x[len(x) - 1])))
	# print('numGuesses: {}'.format(str(numGuesses)))
	# return x[len(x) - 1], numGuesses
	
	
	
# test = compute_root(poly, 3, 0.001)
# print('compute_root(poly, 3, 0.001): {}'.format(str(test)))
	
# Works ()
# Robust ()
# Better Than Expect ()
# Understood () 	
	
	
	
	
	
	





