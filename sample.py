import sys as S
from numpy import random
from histogram import histogram



def sample_by_frequency(count):
  f = open("everyManInHisHumor.txt", "r")
  f = " ".join(f)
  f = f.split()
  h = histogram(f)

  p = []
  i = []
  for k, v in h.items(): 
    p.append(v / 49788) # frequency of words / total words
    i.append(k)
  print(p, i)
  word = random.choice(i, count, p)

  return word