import sys as S
from random import randint

#reads our file
f = open("words.txt", "r")
f = f.read()
f = "".join(f)
f = str(f)
f = f.split(" ")

#sets terminal values
S.argv = S.argv[1]
x = S.argv

def mix(x):
    word = 0
    sentence = []
    while word < x:
        y = randint(0, len(f) - 1)
        sentence.append(f[y])
        word += 1
    sentence = " ".join(sentence)
    print(sentence)

mix(int(x))