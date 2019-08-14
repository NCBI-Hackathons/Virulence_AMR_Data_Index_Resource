from random import random
from random import sample
from random import randint

def rand_str(alph, length): return "".join([sample(alph,1)[0] for _ in range(length)])

alph_meta = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.?!(){}=,"
alph_meta = "abcdefghijklmnopqrstuvwxyz"
alph_meta1 = "".join([sample(alph_meta,1)[0] for _ in range(100)])
alph_meta2 = "".join([sample(alph_meta,1)[0] for _ in range(100)])

alpha_contigs = "GATC"
alpha_contigs1 = "GGGATTC" 
alpha_contigs2 = "GATTCC"

meta_min_length = 10000
meta_max_length = 10000
srr_metas = {}
srr_metas["1"] = rand_str(alph_meta1, randint(meta_min_length, meta_max_length))
srr_metas["2"] = rand_str(alph_meta1, randint(meta_min_length, meta_max_length))
srr_metas["3"] = rand_str(alph_meta2, randint(meta_min_length, meta_max_length))
srr_metas["4"] = rand_str(alph_meta2, randint(meta_min_length, meta_max_length))

contig_min_length = 10000
contig_max_length = 10000
srr_contigs = {}
srr_contigs["1"] = rand_str(alpha_contigs1, randint(contig_min_length, contig_max_length))
srr_contigs["2"] = rand_str(alpha_contigs1, randint(contig_min_length, contig_max_length))
srr_contigs["3"] = rand_str(alpha_contigs1, randint(contig_min_length, contig_max_length))
srr_contigs["4"] = rand_str(alpha_contigs1, randint(contig_min_length, contig_max_length))

def get_meta(srr):
    return srr_metas[srr]

def get_contigs(srr):
    return srr_contigs[srr]

if __name__ == "__main__":
    print(get_meta(1))
    print(get_contigs(4))
