import preprocess as pp
import sys
import lzc_meta
import lzc_contig
import itertools
import time
import gzip

def perms(lA, lB): 
    result = set()
    for a, b in itertools.product(lA, lB):
        pair = tuple(sorted((a, b)))
        result.add(pair)
    return sorted(result)
    
def write_stats(get_txt, C, l, outfile, ids):
    t0 = time.time()
    txt = {iid:get_txt(iid)[:1000000] for iid in ids}
    t1 = time.time()
    print("download time: " + str(t1-t0))
    sC   = {iid:C(txt[iid]) for iid in ids}
    sCAB = {(idA, idB):C(txt[idA]+txt[idB]) for idA, idB in perms(ids, ids) if not idA == idB}
    sl   = {iid:l(txt[iid]) for iid in ids}
    slAB = {(idA, idB):l(txt[idA]+txt[idB]) for idA, idB in perms(ids, ids) if not idA == idB}
    f = open(outfile, 'w')
    sep = '\t'
    f.write("ssrA" + sep + "srrB" + sep + "ncd" + sep)
    f.write("slA" + sep + "sCA" + sep)
    f.write("slB" + sep + "sCB" + sep)
    f.write("slAB" + sep + "sCAB" + sep)
    f.write("\n")
    for a, b in perms(ids, ids):
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

def gzipC(s): return len(gzip.compress(s.encode()))
def gzipl(s): return len(s.encode())

if __name__ == "__main__":
    filename = 'srrs.txt'
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    srrs = [srr.strip() for srr in open(filename).readlines()]
    
    #write_stats(pp.get_meta, gzipC, gzipl, 'meta.txt', srrs)
    #write_stats(pp.get_contigs, gzipC, gzipl, 'contigs.txt', srrs)
    write_stats(pp.get_meta, lzc_meta.C, lzc_meta.l, 'meta.txt', srrs)
    write_stats(pp.get_contigs, lzc_contig.C, lzc_contig.l, 'contigs.txt', srrs)
