try: 
	APY = float(input('GIVE ME YOUR APY: '))
except ValueError:
	
	def apy_except_handler():

		try: 
		
			APY = float(input('Please enter a number for your APY'))
			return APY
			
		except ValueError: 
		
			APY = apy_except_handler()
			return APY
	
	APY = apy_except_handler()
		
print('Pre-percentified APY: ' + str(APY))

''' 

Why does this happen, and what do I do to store the number into APY?

To create an UnboundLocalError:

1. Enter letters when it asks for your APY x 2+ times
2. Enter a number 

Notes:

 - If I put return APY, it gives me a 'None' value. 
 - If I put it after the try-except clause, it'll give the UnboundLocalError 
 
 '''