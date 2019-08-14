# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:22:21 2019

@author: RC
"""
import os


def get_table():

    import pandas as pd

    return pd.read_csv('combined_bq_table.csv', ',', header = 0)


def get_fa(fname):
    
    base_path = 'gs://strides-microbial-datasets/enterococcus/files/'
    
    out = ''
    
    for line in os.popen('gsutil cat ' + base_path + fname).readlines():
        if not line.startswith('>'):
            addition = line.strip().rstrip()
            out += addition
    
    return out

def get_contigs(srr):
    
    tbl = get_table()
    print(tbl.columns)
    tbl = tbl[['acc', 'nucleotide_fasta']]
    fnames = list(tbl[tbl.acc == srr].nucleotide_fasta.values)
    
    cat_fas = ''
    
    for fname in fnames:
        
        try:
            cat_fas += get_fa(fname)
        except:
            print(str(fname)+' failed')
            
    return cat_fas
    
def get_meta(srr):
    
    tbl = get_table()
    tbl = tbl[tbl.acc == srr]
    
    keep = list()
    
    for col in tbl.columns:
        
        if len(tbl[col].unique()) == 1:
            
            keep.append(str(tbl[col].unique()[0]))
            
    return ' '.join(keep)

if __name__ == '__main__':
    print(get_meta('DRR015824'))
    print(get_contigs('DRR015824'))
