This directory contains two experiments related to compression.  In both experiments the Lempel-Ziv (LZ) compression algorithm is used.  The `ncd_exp` uses the normalized compression distance to compare the similarity and metadata and contigs.  The `tf-idf` experiment compares the tf-idf score across multiple contigs for each entry in the respective contig's LZ dictionary.  The LZ dictionary is constructed in the process of running the LZ compression algorithm on the contig. The experiment shows there is a strong correlation between the entry length and its tf-idf score.

The `data` directory contains a number of contigs that can be used for experiments.

Research papers the two experiments are based on can be found in the `research` directory.  The NCD is defined in the "Clustering by Compression" paper and the paper on algorithmic significance explains why long sequences in the dictionary are statistically significant.
