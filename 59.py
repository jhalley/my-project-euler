#!/usr/bin/python

import itertools

def get_words():
    x = {}
    f=open('/usr/share/dict/words', 'r')
    for i in f.readlines():
        x.setdefault(i.strip().lower(), '')
    f.close()
    return x

def get_cipher(file):
    f = open(file, 'r')
    x = [i.strip().split(',') for i in f.readlines()][0]
    f.close()
    return x

def main():
    words = get_words()
    cipher = [int(i) for i in get_cipher('cipher1.txt')]

    for i in itertools.permutations(range(ord('a'), ord('z')+1), 3):    # generate all lower case 3 letter combinations with repeatitions
        j = list(i) * 400 + [i[0]]
        potential = ''.join([chr(cipher[index]^j[index]) for index in range(len(cipher))])

        for k in range(len(potential[:30]) - 6):    # find a word with 6 letters in the first 30 chars
            if potential[k:k+6].lower() in words:
                print ''.join([chr(letter) for letter in i])
                print potential
                print '\n'
                break
                

main()
