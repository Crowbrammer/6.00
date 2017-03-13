# Problem Set 3a
# Name: Aaron Bell
# Time: 5 hours


from ps3a import *
import time
from perm import *
import sys

#
#
# Problem #6A: Computer chooses a word
#
#

def comp_choose_word(hand, word_list):
	"""
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

	hand: dictionary (string -> int)
	word_list: list (string)
	"""
	# TO DO...

	'''

	A. Check the score (X)
	B. Check the score against the next word (X)
	C. If the word is higher value than the current, replace the selection with the word (X)
	D. Get permutations of hand at a certain length (X)
	E. Go through each possible length of permutations (X)
	F. Get the hand (X)
	G. Get the word_dict (X)
	H. Check if a word's in the word_list (X)
	I. return highest_value_word (X)

	'''

	current_best = 0
	selection = ''

	print('Please wait. Computer picking answer...')

	#E
	for n in reversed(range(1, HAND_SIZE + 1)):

		#D
		current_choices = get_perms(hand, n) #F

		#H
		for each in current_choices:

			#H
			if each in word_list:


				current_word_score = get_word_score(each)
				#B
				if current_word_score > current_best: #G

					#C
					current_best = current_word_score
					selection = each

	if selection is not '':
		print('---From comp_choose_word(hand, word_list)---')
		print('The hand is: ' + str(hand))
		print('The computer chooses: ' + selection)
		print('The value of the word is ' + str(get_word_score(selection)))

		#I
		return selection
	else:
		selection = '.'
		return selection
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
	"""
	 Allows the computer to play the given hand, as follows:

	 * The hand is displayed.

	 * The computer chooses a word using comp_choose_words(hand, word_dict).

	 * After every valid word: the score for that word is displayed,
	   the remaining letters in the hand are displayed, and the computer
	   chooses another word.

	 * The sum of the word scores is displayed when the hand finishes.

	 * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

	 hand: dictionary (string -> int)
	 word_list: list (string)
	"""
	# TO DO ...

	total_score = 0

	while len(hand) > 0:

		display_hand(hand)
		comp_guess = comp_choose_word(hand, word_list)
		if comp_guess == '.':
			print('No answer found. Ending round.')
			print('Total score: ' + str(total_score))
			return

		while is_valid_word(comp_guess, hand, word_list) is False and comp_guess is not '.':

			comp_guess = input('The computer picked an invalid word. Press ' \
			'any button to escape this function.')
			if comp_guess == '.': return

		word_score = get_word_score(comp_guess, hand)
		total_score += word_score
		hand = update_hand(hand, comp_guess)
		print('The score for "{}" is {}. Total score: {}'.format(comp_guess, str(word_score), str(total_score)))

	print('The total score for this hand is: {}'.format(str(total_score)))

def player_or_computer(user_input):

	while user_input not in 'uce':
		user_input = input('Would you like to play? ("u") Or do you '\
		'want the computer to play? ("c") Or, press "e" to exit.\n').lower()
	if user_input == 'u':
		return play_hand(hand, word_list)
	elif user_input == 'c':
		return comp_play_hand(hand, word_list)
	elif user_input == 'e':
		print('Thanks for playing!')
		sys.exit()
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
	"""Allow the user to play an arbitrary number of hands.

	1) Asks the user to input 'n' or 'r' or 'e'.
	* If the user inputs 'n', play a new (random) hand.
	* If the user inputs 'r', play the last hand again.
	* If the user inputs 'e', exit the game.
	* If the user inputs anything else, ask them again.

	2) Ask the user to input a 'u' or a 'c'.
	* If the user inputs 'u', let the user play the game as before using play_hand.
	* If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
	* If the user inputs anything else, ask them again.

	3) After the computer or user has played the hand, repeat from step 1

	word_list: list (string)
	"""
	# TO DO...

	user_input = input('New hand ("n") or exit ("e")?\n').lower()

	if user_input == 'e': return

	while True:

		if user_input == 'e':
			return
		elif user_input == 'n':
			hand = deal_hand(HAND_SIZE)
			player_or_computer(user_input)
		elif user_input == 'r':
			player_or_computer(user_input)
		user_input = input('New hand ("n"), play the same hand ("r"), ' \
			'or exit ("e")?\n')
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
	word_list = load_words()
	play_game(word_list)
