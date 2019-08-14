from math import log, ceil
import sys
import os

alphabet = 'gatc'
monocase = True
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
    codeword_len = ceil(log(len(d), 4))
    num_codewords = sum(v for v in d.values())
    comp_len = codeword_len * num_codewords
    return min(len(s), comp_len)

# Syntactic sugar.
def C(x): return calc_c(x, lzd(x))

# Calculate ncd(x,y) or C(x) based on input parameters.
# String may be too short to compress, so compressibility is 'amplified' by repeating.
default_amp = 90
if __name__ == "__main__":
    xf = sys.argv[1]
    yf = None
    if len(sys.argv) > 2:
        yf = sys.argv[2]
    amp = default_amp
    if len(sys.argv) > 3:
        amp = int(sys.argv[3])

    x = open(xf).read()
    if monocase:
        x = x.lower()
    x = [c for c in x if c in alphabet]
    x *= amp
    if yf:
        y = open(yf).read()
        if monocase:
            y = y.lower()
        y = [c for c in y if c in alphabet]
        y *= amp

        print((C(x+y)-min(C(x),C(y)))/max(C(x),C(y)))
    else:
        print(C(x))
