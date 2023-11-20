
import random
from random import choice

val = input(">  ")





##https://stackoverflow.com/questions/4296678/is-there-a-pythonic-way-to-insert-space-characters-at-random-positions-of-an-exi##
def insert_spaces(s):
    s = list(s)
    for i in range(len(s)-1):
        while random.randrange(2):
            s[i] = s[i] + ' '
    return ' '.join(s)

##https://stackoverflow.com/questions/4296678/is-there-a-pythonic-way-to-insert-space-characters-at-random-positions-of-an-exi##


sentence = (''.join(choice(( str.upper, str.lower))(c) for c in val))


print(insert_spaces(sentence))
