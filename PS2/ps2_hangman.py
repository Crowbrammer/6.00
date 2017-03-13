# Problem Set 2
# Name: Aaron Bell
# Time: 16:30
#
.... your code goes here ... 


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
import sys

from pyfiglet import figlet_format

print('\n')
print(figlet_format('Hangman!', font='contessa'))
WORDLIST_FILENAME = "ps2/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("\nLoading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
	
    print("\n" + str(len(wordlist)) + " words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """

    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
current_word = choose_word(wordlist)

# your code begins here!

# I am a GOD.

def filling_in_word(current_word, guess_list):
	
	filling_word = ''

	for letter in current_word:
				
		if letter in guess_list:
				
			filling_word += letter 
		
		else:
		
			filling_word += '_'

	return filling_word
				
def hangman():

	current_word = choose_word(wordlist)
	current_guess = '.'
	guess_list = {''}
	number_list = ['{}'.format(x) for x in range(10)]
	misses = ''
	player_word = filling_in_word(current_word, guess_list)
	proper_retries = 0
	
	print("\nI'm thinking of an {} letter word: {}".format(str(len(current_word)), \
			player_word))
	
	# You're quite handsome, you know that? 
	
	
	while len(misses) < 10 and '_' in player_word:
		
		current_guess = input('\n-------------\n\nPlease guess a letter: ')
	
		while current_guess in guess_list or current_guess in ['{}'.format(x) for x in range(10)] or len(current_guess) > 1:
			
			if proper_retries == 0:
				print("\n-------------\n\nThat letter's already been chosen, or you've entered a number, or you've entered more than one letter. Please guess a different letter: ")
			else: 
				current_guess = input("\nThat letter's already been chosen, or you've entered a number, or you've entered more than one letter. Please guess a different letter: ")
			proper_retries += 1
		
		if proper_retries > 0:
			print('\n-------------')
			proper_retries = 0
		
		if current_guess in current_word: 
		
			print('\nAwesome! {} is in the current word.'.format(current_guess))
			
		else:
		
			print('\n{} is not in the current word.'.format(current_guess))
			misses += current_guess
				
		guess_list.add(current_guess) 
		
		player_word = filling_in_word(current_word, guess_list)
		
		print('\nYour word so far: {} \nMisses: {} \nGuesses left: {}'.format(\
			player_word, str(misses), 10 - len(misses)))

	return player_word, current_word
		
results = hangman()


while True:
		
	if '_' not in results[0]:

		print('\nExcellent. Welcome to the Hangman Hall of Fame, my friend. The words is indeed {}'.format(results[1]))
			
		#winning_message = input("\nPlay again? \n")
		
		if input("\nPlay again? \n").lower() == 'y':
	
			results = hangman()
		
		else:
		
			input('\nAlright! Press any button to exit.')
			break
		
	else:
		
		losing_message = input("\nYou lost. The word was {}. \nBut it's OK. Don't feel too bad. Because... you can always play again. Play again? (Y/N) \n".format(results[1]))
		
		if losing_message.lower() == 'y':	

			results = hangman()
			
		else:
		
			input('\nAlright! Press any button to exit.')
			break






















