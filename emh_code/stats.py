import csv
import sys
import pandas as pd

filename = '../target_srr_metadata.csv'
if len(sys.argv) > 1:
    filename = sys.argv[1]

meta = pd.read_csv(filename)

print(meta.describe())
