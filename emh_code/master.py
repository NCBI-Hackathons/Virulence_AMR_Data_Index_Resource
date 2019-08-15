import preprocess as pp
import sys
import os
import lzc_meta
import lzc_contig
import itertools
import time
import gzip
from multiprocessing.dummy import Pool as ThreadPool
from random import shuffle
from random import randint

def write_stats(get_txt, C, l, outfile, pairs):
    print("starting writing pairs " + str(pairs) + " to " + outfile)
    ids = set()
    for a, b in pairs:
        ids.add(a)
        ids.add(b)
    t0 = time.time()
    txt = {iid:get_txt(iid) for iid in ids}
    t1 = time.time()
    print("download time: " + str(t1-t0) + " " + outfile)
    t0 = time.time()
    sC   = {iid:C(txt[iid]) for iid in ids}
    t1 = time.time()
    print("singleton time: " + str(t1-t0) + " " + outfile)
    t0 = time.time()
    sCAB = {(idA, idB):C(txt[idA]+txt[idB]) for idA, idB in pairs if not idA == idB}
    t1 = time.time()
    print("pair time: " + str(t1-t0) + " " + outfile)
    sl   = {iid:l(txt[iid]) for iid in ids}
    slAB = {(idA, idB):l(txt[idA]+txt[idB]) for idA, idB in pairs if not idA == idB}
    f = open(outfile, 'w')
    sep = '\t'
    f.write("ssrA" + sep + "srrB" + sep + "ncd" + sep)
    f.write("slA" + sep + "sCA" + sep)
    f.write("slB" + sep + "sCB" + sep)
    f.write("slAB" + sep + "sCAB" + sep)
    f.write("\n")
    for a, b in pairs:
        if a == b: continue
        # Output NCD for pair
        ncd = (sCAB[(a, b)] - min(sC[a], sC[b]))/max(sC[a], sC[b])
        f.write(a + sep + b + sep + str(ncd) + sep)
        # Output rest of stats
        f.write(str(sl[a]) + sep + str(sC[a]) + sep)
        f.write(str(sl[b]) + sep + str(sC[b]) + sep)
        f.write(str(slAB[(a,b)]) + sep + str(sCAB[(a,b)]) + sep)
        f.write("\n")
    f.close()
    print("wrote pairs " + str(pairs) + " to " + outfile)

def meta_wrap(id_pairs): 
    iid, pairs = id_pairs
    write_stats(pp.get_meta, lzc_meta.C, lzc_meta.l, 'meta' + str(iid) + '.txt', pairs)
def contigs_wrap(id_pairs): 
    iid, pairs = id_pairs
    write_stats(pp.get_contigs, lzc_meta.C, lzc_meta.l, 'contigs' + str(iid) + '.txt', pairs)

if __name__ == "__main__":
    filename = [f for f in os.listdir('.') if 'pairs.txt' in f][0]
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    pairs = [tuple(pair.strip().split(' ')) for pair in open(filename).readlines()]
    shuffle(pairs)
    split_size = 5 
    pairs_splits = [(randint(0, 100000000), pairs[i:i+split_size]) for n, i in enumerate(range(0, len(pairs), split_size))]
    pool = ThreadPool(8)
    pool.map(contigs_wrap, pairs_splits)
