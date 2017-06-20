# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift, alphabet='abcdefghijklmnopqrstuvwxyz ', ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ '):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',v
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    ### TODO.

    shifted = dict()

    modu = 27
    if shift < 0: modu = -27

    for each in alphabet:
        shifted[each] = alphabet[(alphabet.find(each) + shift) % modu]
    for EACH in ALPHABET:
        shifted[EACH] = ALPHABET[(ALPHABET.find(EACH) + shift) % modu]

    return shifted

# print(build_coder(-10))

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)

    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.

    # They want the exact same thing that build_coder does. So just call that
    # using the current shift argument for the build_coder shift argument.

    return build_coder(shift)

def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)

    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.

    '''
    Generate a new alphabet based the shift key
    Pass the new alphabet into build_coder along with the negative shift key-value
    Return the value that build_coder does.
    '''

    # 1. Generate a new alphabet based the shift key

    # Take on alphabet string
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

    # Remember if shift is negative or positive

    # if shift is positive, take the value of modulo 27 shift, and
    # get a value to it
    modu = 27
    if shift <= 0: modu = -27
    # print('\nHYPOTHESIS:\n')
    # print('I predict this will produce a "rstuvwxyz abcdefghijklmnopq" alphabet.')
    #
    # print('\nEXPERIMENT RESULTS:\n')
    alphabet = alphabet[shift % modu:] + alphabet[:shift % modu]
    ALPHABET = ALPHABET[shift % modu:] + ALPHABET[:shift % modu]
    # print('alphabet[shift % modu:] + alphabet[:shift % modu]:', alphabet)
    # print('ALPHABET[shift % modu:] + ALPHABET[:shift % modu]', ALPHABET)

        # print('\nHYPOTHESIS:\n')
        # print('I predict this will produce a "klmnopqrstuvwxyz abcdefghij" alphabet.')
        #
        # print('\nEXPERIMENT RESULTS:\n')
        # alphabet = alphabet[shift % 27:] + alphabet[:shift % 27]
        # ALPHABET = ALPHABET[shift % 27:] + ALPHABET[:shift % 27]
        # print('alphabet[shift % 27:] + alphabet[:shift % 27]:', alphabet)
        # print('ALPHABET[shift % 27:] + ALPHABET[:shift % 27]', ALPHABET)

        # alphabet += alphabet[0:shift]
        # alphabet = alphabet[shift:]
        # ALPHABET += ALPHABET[0:shift]
        # ALPHABET = ALPHABET[shift:]

        ### TEST part
        # print('Alphabet:', alphabet)
        # print('Backward:', alphabet[:shift])
        # print('[A:]', alphabet[shift:])
        # print('[:-A]', alphabet[:-shift])
        # if alphabet[shift:] == alphabet[:-shift]:
        #     print('alphabet[shift:] == alphabet[:-shift]')
        # else:
        #     print('alphabet[shift:] != alphabet[:-shift]')
        # updated_alphabet = ''
        # alphabet += alphabet[:shift]
    #     # alphabet = alphabet[shift:]
    #     # print('Alphabet:', alphabet)
    #
    #     # THAT, is the sexiest code anyone ever did saw. No variables/reassignment.
    #     # Just clean, direct code
    # # if shift is negative, take the value of modulo -27 shift, and
    # # get a value to it
    # else:
    #
    #     # Slice the end of the string part back unitl the length of the shift modulo 27
    #     # and move it to the beginning of the alphabet
    #
    #
    #     # print('\nHYPOTHESIS:\n')
    #     # print("For -18, I expect jklmnopqrstuvwxyz abcdefghi")
    #     # print("I predict that Python won't through out the original alphabet object \
    #     #     until it moves onto the next line.")
    #     # print('But, I also predict an error with the expression in the slice operator')
    #     #
    #     # print('\nEXPERIMENT RESULTS:\n')
    #     # print('alphabet[shift:]:', alphabet[shift:])
    #     # print('alphabet[:shift+27]:', alphabet[:shift+27])
    #     # print('\nHYPOTHESIS:\n')
    #     # print('I predict this -64 shift will produce a "rstuvwxyz abcdefghijklmnopq" alphabet.')
    #     #
    #     # print('\nEXPERIMENT RESULTS:\n')
    #     alphabet = alphabet[shift % -27:] + alphabet[:shift % -27]
    #     ALPHABET = ALPHABET[shift % -27:] + ALPHABET[:shift % -27]
    #     # print('alphabet[shift % -27:] + alphabet[:shift % -27]:', alphabet)
        # print('ALPHABET[shift % -27:] + ALPHABET[:shift % -27]', ALPHABET)
        # print(alphabet)

    # 2. Pass the new alphabet into build_coder along with the negative shift key-value, AND
    # 3. Return the value that build_coder does.

    return build_coder(-shift, alphabet, ALPHABET)

    # Use the same process for creating a shifted dictionary. But, use the negative
    # of the shift

#     shifted = dict()
#     for each in alphabet:
#         shifted[each] = alphabet[(alphabet.find(each) + shift) % 27]
#     for EACH in ALPHABET:
#         shifted[EACH] = ALPHABET[(ALPHABET.find(EACH) + shift) % 27]
#
#     return shifted

# print('\nHYPOTHESIS:\n')
# print('I predict this code will provide me the correct dictionary needed to decode a 10-shifted sentence.')
# print("10: 'm' > 'c', 'k' > 'a', 'l' > 'b'")
#
# print('\nEXPERIMENT RESULTS:\n')
# print(build_decoder(10))
#
# print('\nHypothesis confirmed!')

# build_decoder(-64)

# print('\nHYPOTHESIS:\n')
# print("I predict this code will NOT print the end of the for loop each time--i.e. \
#     pass only works on functions -- but continue works")

# print('\nEXPERIMENT RESULTS:\n')
# for each in range(10):
#     print('I should be here.')
#     pass
#     print("I shouldn't be here.")

# print('\nHYPOTHESIS:\n')
# print("I predict this code will print a sorted dictionary where 'a':'d', 'b':'e'")

# print('\nEXPERIMENT RESULTS:\n')
#print(sorted(build_encoder(-10).items()))

def apply_coder(text, coder, char_index=0):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    ### TODO.

    # Grab the text, dictionary from build_encoder()

    ###
    #if char_index == 0:
        #print('\nHYPOTHESIS:\n')
        #print('I predict this will correctly shift each letter and return ciphertext')
        # print('I predict this will print to just after the third letter.')

        #print('\nEXPERIMENT RESULTS:\n')
        # print('3rd letter:', 'Hello'[3])
        # print('Slice to just after 3rd letter:', 'Hello'[:3])
        ###

    plaintext = text

    if char_index == len(plaintext) - 1:
        # Return the shifted the character and return
        if plaintext[char_index] in 'abcdefghijklmnopqrstuvwxyz ' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            #print('char_index at {}:'.format(char_index), coder[plaintext[char_index]])
            return coder[plaintext[char_index]]
        else: return plaintext[char_index]

    else:
        # Return shifted character + this function again, with char-index+1
        if plaintext[char_index] in 'abcdefghijklmnopqrstuvwxyz ' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            #print('char_index at {}:'.format(char_index), coder[plaintext[char_index]])
            return coder[plaintext[char_index]] + apply_coder(text, coder, char_index + 1)
        else: return plaintext[char_index] + apply_coder(text, coder, char_index + 1)

    # # For each character in the text:
    # for char_index in range(len(plaintext)):
    #     # If a letter, shift it
    #     if plaintext[char_index] in 'abcdefghijklmnopqrstuvwxyz ' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    #         # Match the current letter to the key in the build_encoder() dictionary
    #         # Replace the letter with the corresponding value from the dictionary
    #         plaintext = plaintext[0:char_index] + coder[plaintext[char_index]] + plaintext[char_index+1:]

    # # Return the new sentence when done
    # ciphertext = plaintext
    # return ciphertext

# Example call


def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    ### TODO.

    return apply_coder(text, build_encoder(shift), char_index=0)

# print('\nHYPOTHESIS:\n')
# print('I predict this code will properly shift the text by 3.')
#
# print('\nEXPERIMENT RESULTS:\n')
# print(apply_shift('Hello, my dear sir!', build_encoder(3)))

#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    ### TODO

    # NOTES
    # If there's no spaces, go to the next shift?

    # Variables

    new_text = text
    correct_words = 0
    current_start = 0
    current_end = 0
    current_shift = 0
    has_spaces = True
    # # If beginning is not a space...
    # if text[0:1] != ' ':

    # print('\nHYPOTHESIS:\n')
    # print("I predict the <<<while text[current_end:current_end + 1] != ' ':>>> loop is giving me problems, because there is no space after the last word.")
    # print("I also predict my tuplified fix won't work.")
    # print("I predict my new boolean language will work")

    # print('\nEXPERI/MENT RESULTS:\n')

    ### Assume there's no space(s) at the beginning for now.
    # print('<<< while correct_words < 3 and current_end < 40: >>> (Loop Started)')

    while correct_words < 3 and current_end < 1000: # While not English words

        # Test if there are spaces in the text
        if ' ' not in new_text:
            current_shift += 1
            new_text = apply_coder(text, build_decoder(current_shift))
            # print("new_text after shift of {}:".format(str(current_shift)), new_text)
            continue


        #print('\nHYPOTHESIS:\n')
        #print("I predict this will give me a series of incomplete words--building up to complete words.")

        #print('\nEXPERIMENT RESULTS:\n')
        #print('text: ' + text)
        #print('text[current_end:current_end + 1]: ' + text[current_end:current_end + 1])
        #print('current_end ==', current_end)

        # print("<<< while end_word != ' ' and end_word != '!' and end_word != '.': >>> (Loop Started)")

        end_word = new_text[current_end:current_end + 1]
        while end_word != ' ' and end_word != '!' and end_word != '.' and end_word != '':

        # while ' !.' not in ....

            current_end += 1

            # I predict I won't need this.

            end_word = new_text[current_end:current_end + 1]

            #print("end_word: '" + end_word + "'")
            #print("current_end:", current_end)
        #     print('text[current_end:current_end]: ' + text[current_end:current_end])
        #
        # print('<<< while new_text[current_end:current_end + 1] != ' ': >>> (Loop Ended)')
        # print('new_text[current_start:current_end] ==', new_text[current_start:current_end])
        # print('correct_words:', correct_words)

        current_word = new_text[current_start: current_end]

        # print("current_word:", current_word)
        # print("is_word(current_word, wordlist):", is_word(wordlist, current_word))

        if is_word(wordlist, current_word):
            correct_words += 1

        current_start, current_end = current_end + 1, current_end + 1


        # If it's at the last word, need to shift up and reset everything
        if end_word == '':
            correct_words, current_start, current_end = 0, 0, 0
            current_shift += 1
            new_text = apply_coder(text, build_decoder(current_shift))



    # print('<<< while current_end < 40: >>> (Loop Ended)')

    if correct_words >= 3: return current_shift
    else:
        current_shift += 1
        correct_words = 0

    # print('<<< while correct_words < 3 and current_end < 40: >>> (Loop Ended)')
# print('\nHYPOTHESIS:\n')
# print("I predict this code will not give me the best shift for these words.")
# print("I think it won't work for text with under 3 words")
# print("I believe it will break if the text uses multiple spaces per word")
#
# print('\nEXPERIMENT RESULTS:\n')
# print("find_best_shift(wordlist, apply_coder('Hello, my fair world.', build_encoder(12)) ==> " + str(find_best_shift(wordlist, apply_coder('Hello, my fair world. I wonder how long this text can be before it breaks.', build_encoder(12)))))



    #
    # #
    # current_end += 1
    # if text[current_end:current_end + 1] == ' ':
    #     if is_word(text[current_start:current_end], wordlist):
    #         correct_words += 1
    #         prior_space_index = current_end + 1
    #         if correct_words >= 3
    #         else:

    # Best function:
    # 	Shift the text
    # apply_shift(text, -1)

    # 	Recognize words function:\
    # 		Select text until a space - if it matches a word, go to spot after the space, and select it until just



    # while beginning = 0 or has_space_before_it AND has_no_space_after:
    #     Increase the length from start by 1
    #     Check if the slice of the end - 1 == a space
    #     If so, break
    # Check the current block of text and see if it's a word.

    #         before the next space. If it matches a word, repeat this.
    # 		If it returns 3 matching words, return True
    # 		Else return False
    # 	If Recognize words function, return current text
    # 	Else return Best function with current text
    # Go back to step #2

#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.
    s = text
    for each in shifts:
        s = s[0:each[0]] + apply_shift(s[each[0]:], each[1])
    return s

#print(apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)]))
#print("deshifted from 0 to 4:", apply_coder())

#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text, start=0):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)

    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """


    print('\nHYPOTHESIS:\n')
    print("I predict that this whole thing will work now.")

    print('\nEXPERIMENT RESULTS:\n')


    # 1. for every possible shift from 0 to 27 
    for each in range(0, 27):
    # 2. set s to be (the text up until just before the start parameter) concatenated with (the text after the  start parameter shifted by the current possible shift) 
        current_shift = each
        s = text[0:start] + apply_coder(text[start:], build_decoder(current_shift))
        print("current_shift:", current_shift)
        print("s:", s)
    # 3. look for spaces beginning at the location specified by the start parameter 
        # print('\nHYPOTHESIS:\n')
        # print("I predict that my changing the range from range(len(s[start:])) to range(len(s[start:]), len[s])... ")
        # print("\n...caused my original start coordinates to go off-kilter")
        #
        # print('\nEXPERIMENT RESULTS:\n')

        for each in range(start, len(s)):
            # print("s[start:]", s[start:])
            #current_place = each
    # 4. if there was a space found and the characters from the start location to the location where the space  was found form a valid word then 
            # if s[each] == ' ':
            #     print('SPACE FOUND')
            #     print("start:", start)
            #     print("each:", each)
                #print("s[0:2]:", text[0:2])
                # print("Is text[start:each] a word:", is_word(wordlist, s[start:each]))
            if s[each] == ' ' and is_word(wordlist, s[start:each]):

                #for each in range(len())
                # print('\nHYPOTHESIS:\n')
                # print("I predict the issue is because I'm not checking until there's not a word, and then recording what the shift is.")
                # print("I predict there will be a bug with this.")
                # Check until there's not a word
                # Record the current shift and starting position in a tuple
                # Record the rest

                # print('\nEXPERIMENT RESULTS:\n')
    # 5. we recursively run this same algorithm on the same text, but starting at the location where the space  was found. 
                #print('\n\nConditional 1 Ran.\n\n')
                # print("start:", each + 1)

                new_algo = find_best_shifts(wordlist, s, each + 1)
    # 6. If this recursive call to the function produces a list of tuples, then that means one of the recursive calls  found the last word properly and we simply prepend a tuple with the start parameter and the current  shift tried to the list and return it. 
                # print("type(new_algo):", type(new_algo))


                if type(new_algo) == list:
                    #print('\n\nConditional 1.5 Ran.\n\n')
                    return [(start, current_shift)] + new_algo

    # 7. If this recursive call to the function produces None, then that means that there was not combination  of shifts and positions found that could produce a valid word at the end, so the error in the shift must  either be in the current call to the function, or an earlier call.  Continue trying all possible shifts (line 1) 
                #elif new_algo == type(None):
    # 8. if there was NOT a space found and the characters from the start location to the end of the string  form a word, then that means we have found a valid shift on this call, so return a list containing a tuple  containing the start parameter and the current shift. 

        # if len(s) < 10: print(">>>Is {} a word?".format(s[start:]), is_word(wordlist, s[start:]))
        if is_word(wordlist, s[start:]):
            #print('\n\nConditional 2 Ran.\n\n')
            #print([(start, each)])

            return [(start, current_shift)]
    # 9. if there was NOT a space found and the characters from the start location to the end of the string do  NOT form a word, then we need to try another shift in this call. 
        else:

            print('\n\nConditional 2.5 Ran.\n\n')
    # # Check for the maximum # of words with current text  (text separated by spaces)
    # max_current_valid_words = 1
    # for each in text: if each == ' ': max_current_valid_words += 1
    #
    # # Check # of real words - keep track
    # num_real_words = 0
    # word_start = 0
    # word_end = 0
    #
    # # for each shift - select the shift with the highest number of words
    # for each in range(-27, 27)
    #
    #     for each in len(text):
    #         if text[each] == ' ':
    #             if is_word(wordlist, text[word_start:word_end]):
    #                 num_real_words += 1
    #             word_start = each + 1
    #
    #         word_end = each
    #
    #     if num_real_words > greatest_num_real_words_current_shift: best_shift = each
    #
    #
    # # Set the new beginning after the space of the last real word
    # # Repeat 1-4 until the end of the text

#shifts = find_best_shifts(wordlist, 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?')
#shifts = find_best_shifts(wordlist, "Do Sevif vjrKylhtgvmgLslj ypjgZollw?", start=3)
# shifts = find_best_shifts(wordlist, "Do AndroIds TguqbpdvpUausIgyspHxuue?", start=12)
# shifts = find_best_shifts(wordlist, "Do AndroIds Dream of ElecTric Sheep?", start=18)
#print("shifts:", shifts)

def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.z

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    ### TODO.


def decrypt_fable():
    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.

    print('\nHYPOTHESIS:\n')
    print("Assuming, get_fable_string() works, I predict that this whole thing will work now. But I believe that get_fable_string() will not work.")

    print('\nEXPERIMENT RESULTS:\n')

    shifts = find_best_shifts(wordlist, get_fable_string())
    for x in shifts:
        if not int: shifts += (x[0], -x[1])
    #print("shifts:", shifts)

    return apply_shifts(get_fable_string(), shifts)

print(decrypt_fable())


#What is the moral of the story?
#
#
#
#
#
