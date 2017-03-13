def evaluate_poly(poly, x):

	f = (0.0,)
	
	try: 
	
		for a in range(len(poly)):
			
			try: 
			
				f +=  (poly[a]*x**a,)
			
			except TypeError: 
			
				print('str(checker(f)) isn*t working')
		
	except TypeError:
	
		f = (poly,)
	
	# Check if there's something 'not right' in the tuple. 
	
	if checker(f): 
	
		return f
		
	else:
	
		return "There's a bogey in the tuple."
	
# DRY the code wit a checker function. Makes sure everything is of a float type. 
	
def checker(checkee, t=float):
	
	return all(isinstance(x, t) for x in checkee)
	

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x = 6

print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))