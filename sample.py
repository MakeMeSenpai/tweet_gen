# from random import randint
from numpy import random
text = 'one fish two fish red fish blue fish'

# [code that converts keys to values goes here aka import histogram] 

word_counts = {'one': 1, 'fish': 4, 'two': 1,
               'red': 1, 'blue': 1}


def sample_by_frequency(h):
    p = []
    i = []
    for k, v in h.items():
      p.append(v / 8)
      i.append(k)
    word = random.choice(i, 1, p)

    # h = h.split()
    # word = h[randint(0, 7)]

    return str(word)

print(sample_by_frequency(word_counts)) #text