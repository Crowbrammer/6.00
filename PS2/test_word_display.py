# test.py

#  You should also display to the user the partially

current_word = 'rhythm'
guesses = ['h', 't']

# Add to the guesses 

filling_in_word = ''

for letter in current_word:
			
	if letter in guesses:
			
		filling_in_word += letter 
	
	else:
	
		filling_in_word += '_'
		

print(filling_in_word)
		