import csv

meta_reader = csv.reader(open('../target_srr_metadata.csv'))

row = next(meta_reader)
row = next(meta_reader)

print row
