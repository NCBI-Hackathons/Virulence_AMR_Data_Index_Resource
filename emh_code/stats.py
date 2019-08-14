import csv
import pandas as pd

meta = pd.read_csv('../target_srr_metadata.csv')

meta.describe()
