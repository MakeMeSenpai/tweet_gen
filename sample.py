import sys as S
#from random import randint
from numpy import random
from histogram import histogram

#checks whether the file was called with a variable
def file_input():
  argv = None
  if len(S.argv) == 2:
    argv = S.argv[1]
#you can return multiple values just with a ','; However this saves as a tuple, so we'll turned it into a list
    return [str(argv), str(True)]
  return [str(argv), str(False)]


def bysample():
  values = ' '.join(file_input())
  values = values.split()
  argv = values[0]
  if values[1] == "False":
    h = histogram(None, True)
    return h
  elif ".txt" in argv:
    h = histogram(argv, True)
    return h
  else:
    return "Unaccepted input, must contain ```$python3 sample.py [example.txt](optional input)```"

def sample_by_frequency():
  h = bysample()

  #checks if h is a dict or a string. if dict run program, else diplay string
  if isinstance(h, dict):
    p = []
    i = []
    for k, v in h.items(): 
      p.append(v / 8)
      i.append(k)
    word = random.choice(i, 1, p)

    # just another solution using randint
    # h = h.split()
    # word = h[randint(0, 7)]

    return str(word)
  return h

#runs our program!... but twice for some reason
print(sample_by_frequency())