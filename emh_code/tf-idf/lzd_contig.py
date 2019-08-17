from math import log, ceil
import sys
import os
from random import shuffle

alphabet = 'gatc'

# Create a subsequence frequency dictionary using the Lempel-Ziv technique.
def lzd(s, d_init={k:0 for k in alphabet}):
    d = dict(d_init.items())
    i = 0
    for n in range(1, len(s)):
        if not s[i:n] in d:
            d[s[i:n]] = 0
            d[s[i:n-1]] = d.get(s[i:n-1], -1) + 1
            i = n
        if n % 100000 == 0: print(n)
    return d

# Write the LZ dict for opened file.
if __name__ == "__main__":
    dna_file = sys.argv[1]
    print("opening "+dna_file)
    x = open(dna_file).read().lower()
    x = ''.join([c for c in x if c in alphabet])
    print("creating dictionary for "+dna_file)
    xd = lzd(x)
    print("writing dictionary for "+dna_file)
    of = open(dna_file+".dict","w")
    for t, v in sorted(xd.items()):
        of.write(t + " " + str(v) + "\n")
    of.close()
    print("completed decomposition for "+dna_file)
