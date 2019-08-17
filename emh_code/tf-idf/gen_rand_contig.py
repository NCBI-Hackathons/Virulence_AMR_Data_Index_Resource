import sys
from random import sample

def rand_str(alph, length): return "".join([sample(alph,1)[0] for _ in range(length)])

if __name__ == "__main__":
    alph = 'gatc'
    length = 4000000
    print(rand_str(alph, length))
