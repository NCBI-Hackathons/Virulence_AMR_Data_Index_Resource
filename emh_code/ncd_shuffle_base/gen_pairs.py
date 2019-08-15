import itertools
import sys

def perms(lA, lB):
    result = set()
    for a, b in itertools.product(lA, lB):
        pair = tuple(sorted((a, b)))
        result.add(pair)
    return sorted(result)

if __name__ == "__main__":
    filename = "srrs.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    f = open(filename)
    srrs = set()
    for line in f.readlines():
        srrs.add(line.strip())
    f.close()

    filename = "pairs.txt"
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    f = open(filename, 'w')
    for pair in perms(srrs, srrs):
        a, b = pair
        if a == b: continue
        f.write(" ".join(pair) + "\n")
    f.close()
