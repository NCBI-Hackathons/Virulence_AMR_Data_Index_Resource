import preprocess as pp
import sys

def perms(lA, lB): return set(sorted(a, b) for a, b in zip(lA, lB))
    
def write_stats(get_txt, outfile, ids):
    txt = {iid:get_txt(iid) for iid in ids}
    txt[None] = ""
    sC = {(idA, idB):lzc.C(txt[idA]+txt[idB]) for idA, idB in perms([ids, ids + [None]])}
    sl = {(idA, idB):lzc.l(txt[idA]+txt[idB]) for idA, idB in perms([ids, ids + [None]])}
    f = open(outfile, 'w')
    sep = '\t'
    for a, b in perms(ids, ids):
        # Output NCD for pair
        ncd = (sC[(a, b)] - min(sC[(a, None)], sC[(b, None)]))/max(sC[(a, None)], sC[(b, None)])
        f.write(a + sep + b + str(ncd) + sep)
        # Output rest of stats
        f.write(str(sl[(a, None)]) + sep + str(sC[(a, None)]) + sep)
        f.write(str(sl[(a, None)]) + sep + str(sC[(a, None)]) + sep)
        f.write(str(sl[(a, b)]) + sep + str(sC[(a, b)]) + sep)
    f.close()

if __name__ == "__main__":
    filename = 'srrs.txt'
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    srrs = [srr.strip() for srr in open(filename).readlines()]
    
    write_stats(pp.get_meta, 'meta.txt', srrs)
    write_stats(pp.get_contigs, 'contigs.txt', srrs)
