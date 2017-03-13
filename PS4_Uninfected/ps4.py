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

def apply_coder(text, coder):
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

#     ###
#     print('\nHYPOTHESIS:\n')
#     print('I predict this code will NOT correctly print letters and avoid symbols.')
#
#     print('\nEXPERIMENT RESULTS:\n')
#     ###
#
#     # For each character in the text:
#     for each_char in 'abcdefghijklmnopqrstuvwxyz ':
#         # If not a letter, continue
#         if each_char not in ('abcdefghijklmnopqrstuvwxyz ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'): continue
#         print(each_char)
#         # Match the current letter to the key in the build_encoder() dictionary
#         # Repalce the letter with the corresponding value from the dictionary
#
#     # Return the new sentence when done
#
# apply_coder('Hi', build_encoder(3))

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

#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
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

def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

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




#What is the moral of the story?
#
#
#
#
#
