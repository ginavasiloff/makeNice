#!/bin/python

from functools import reduce

notNice = open('nice.txt', 'r')
nice = open('nicer.txt', 'w')

makeIt = "nice"
max = len(makeIt)
n=0

def nice_char(char):
    global n
    global nice
    code = ord(char)
    idx = n%max

    if 97 <= code <= 122:
        nice_char = makeIt[idx]
        n += 1

    elif 65 <= code <= 90:
        nice_char = makeIt[idx].upper()
        n += 1

    else:
        nice_char = char
    
    return nice_char


for line in notNice:
    nice.write(reduce( lambda acc, item: acc + nice_char(item), line ))
