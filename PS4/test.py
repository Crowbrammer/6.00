'''

MANUAL EXPERIMENT RESULTS:

Shifts:
3,
10
-10

New Alphabets:
defghijklmnopqrstuvwxyz abc
klmnopqrstuvwxyz abcdefghij
rstuvwxyz abcdefghijklmnopq

Negative Shifts:
-3
-10
10

Dictionaries:
For 3 >>> 'd':'a', 'e':'b', 'f':'c'...'a':'y', 'b':'z', 'c':' '
For 10 >>> 'k':'a', 'l':'b', 'm':'c'...'a':'r', 'b':'s', 'c':'t'
For -10 >>> 'r':'a', 's':'b', 't':'c'...'a':'k', 'b':'l', 'c':'m'

Real Word:
'cab'

Ciphertext:
3 >>> fde
10 >>> mkl
-10 >>> trs

Plaintext:
3:
'f' > 'c'
'd' > 'a'
'e' > 'b'
10:
'm' > 'c'
'k' > 'a'
'l' > 'b'
-10:
't' > 'c'
'r' > 'a'
's' > 'b'

So have the original code return a shifted alphabet, too.
Have coder and coder accept an alphabet
Run coder

$68,493.16

'''

print(-100 % 9)

'''

Experience the character going through all these pains and struggles.
My heart continues to beat.
My heart continues to beat.
My heart continues to beat.

'''
alphabet = 'abcdefghijklmnopqrstuvwxyz '
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
shifted = dict()

for each in alphabet:
      shifted[each] = alphabet[(alphabet.find(each) + -10) % -27]
for EACH in ALPHABET:
      shifted[EACH] = ALPHABET[(ALPHABET.find(EACH) + -10) % -27]
print(shifted)
