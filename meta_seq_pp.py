# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:22:21 2019

@author: RC
"""


def get_table():

    import pandas as pd

    return pd.read_csv('target_srr_metadata.csv', ',', header = 0)


def get_fa(fname):
    
    base_path = 'gs://strides-microbial-datasets/enterococcus/files/'
    
    out = ''
    
    with open(base_path+fname) as f:
        for line in f:
            if not line.startswith('>'):
                addition = line.strip().rstrip()
                out += addition
    
    return out

def seq_pp(srr):
    
    tbl = get_table()[['acc', 'nucleotide_fasta']]
    fnames = list(tbl[tbl.acc == srr].nucleotide_fasta.values())
    
    cat_fas = ''
    
    for fname in fnames:
        
        try:
            cat_fas += get_fa(fname)
        except:
            print(str(fname)+' failed')
            
    return cat_fas
    
def meta_pp(srr):
    
    tbl = get_table()
    tbl = tbl[tbl.acc == srr]
    
    keep = list()
    
    for col in tbl.columns:
        
        if len(tbl[col].unique()) == 1:
            
            keep.append(str(tbl[col].unique()))
            
    return ' '.join(keep)

if __name__ == '__main__':
    
    print('Import me!')
            
    