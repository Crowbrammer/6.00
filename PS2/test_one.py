def evaluate_poly(poly, x):

	f = (0.0,)
	
	try: 
	
		for a in range(len(poly)):
			
			try: 
			
				f +=  (poly[a]*x**a,)
				print('f12: ' + str(f))
				print(str(all(isinstance(x, float) for x in f)) + ' at Line 156')
				
			
			except TypeError: 
			
				print('str(all(isinstance(x, float) for x in f)) isn*t working')
				print('f18: ' + str(f))
				print(str(all(isinstance(x, float) for x in f)) + ' at Line 161')
		
	except TypeError:
	
		f = (poly,)
		print('f24: ' + str(f))
		print(str(all(isinstance(x, float) for x in f)) + ' at Line 166')
	
	print('f27: ' + str(f))
	print(str(all(isinstance(x, float) for x in f)) + ' at Line 169') 
	
	if all(isinstance(x, float) for x in f): 
	
		return f
		
	else:
	
		return "There's a bogey (string or something) in the tuple."
	
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x = 6

print('evaluate_poly(poly, x): ' + str(evaluate_poly(poly, x)))


# What the code represents. Also a test to compare the code's answer to. 
print('f(6) = 5.0(6)**2 + 9.3(6)**4 + 7.0(6)**5: ' + str((5.0*(x)**2 + 9.3*(x)**4 + 7.0*(x)**5)))

'''

Word problems 
Complicated problems in the sciences
basic Chemistry
basic Physics
Economics (Cost analysis)
Social Sciences
(Calculus)
(Numerical Analysis)
Construction
Meteorology
Rollercoaster design 
Bridges


'''