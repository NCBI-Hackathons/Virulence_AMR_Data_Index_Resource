from math import log, ceil
import sys
import os

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

# Calculate C(x) based on input parameters.
if __name__ == "__main__":
    dna_dir = sys.argv[1]
    seqs = {}
    tf = {}
    idf = {}
    tfidf = {}
    dsz = 0
    for d, xf in enumerate(os.listdir(dna_dir)):
        x = open(dna_dir+xf).read()
        x = x.lower()
        x = ''.join([c for c in x if c in alphabet])
        seqs[d] = x
        xd = lzd(x)
        dsz += len(xd)
        sig = ceil(log(len(xd), len(alphabet)))
        for t, v in xd.items():
            if len(t) > sig and v > 0:
                tf[(t, d)] = tf.get((t, d), 0) + 1
                idf_cnt = idf.get(t, set())
                idf_cnt.add(d)
                idf[t] = idf_cnt
    N = len(seqs)
    for t, idf_cnt in idf.items():
        idf[t] = log(N,2)-log(len(idf[t]),2)
    for d in seqs.keys():
        for t in idf.keys():
            tfidf[(t,d)] = tf.get((t,d),0)*idf[t]
    sig = ceil(log(dsz,4))
    for k, v in sorted(tfidf.items(), key=lambda x:x[1], reverse=False):
        print(len(k[0])-sig,v)
