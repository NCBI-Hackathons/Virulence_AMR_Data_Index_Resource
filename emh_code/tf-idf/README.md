Run tdidf and sequence length comparison with
```
python3 lzd_contig.py data/
```
It will create dictionaries for all the dna in the `data` directory, and then compute the tf-idf for all the terms across all the dictionaries.  Finally, the script will calculate the average sequence length for each tf-idf score, and outputs each score and average length pair.  These can then be plotted to visualize the relationship. 

The analysis has been run for both real DNA sequences and randomly generated synthetic sequences.  The difference in correlation between kmer length and tf-idf scores can be seen in the images folder.
