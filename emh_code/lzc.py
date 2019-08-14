from math import log, ceil
import sys
import os

alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
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
    return d

# Use the dictionary to calculate string compression.
def calc_c(s, d):
    codeword_len = ceil(log(len(d), len(alphabet)))
    num_codewords = sum(v for v in d.values())
    comp_len = codeword_len * num_codewords
    return min(len(s), comp_len)

# Syntactic sugar.
def C(x): return calc_c(x, lzd(x))

# Calculate C(x) based on input parameters.
if __name__ == "__main__":
    xf = sys.argv[1]
    x = open(xf).read()
    x = x.lower()
    x = ''.join([c for c in x if c in alphabet])
    print(len(x), C(x))
