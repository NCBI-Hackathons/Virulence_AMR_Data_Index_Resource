# Virulence_AMR_Data_Index
Indexing and Visualization for AMRs and Virulence Genes in Genomes and Metagenomes

# Purpose
Develop a tool capable of evaluating metadata quality in the Sequence Read Archive (SRA), together with the contigs assembled from each of the runs (SRRs).

Provide visualization capabilities to assist in downstream interpretation.

Use cases:
1. Find accession/contig by taxonomy
2. Find accessions/contig by gene (drug resistance, virulence factor)
3. Find accession/contig by genes cluster
4. Find accession/contig by domain
5. Find accession by host
6. Find similar SRR/contigs
7. Find accession/contig by seuqence

# Workflow
The overarching framework of our approach is to enable the integration of various metadata types in a large data structure that consists of multiple tables. An example of such a framework and the various data types that can be supported can be seen below.
![Metadata Pipeline](https://raw.githubusercontent.com/NCBI-Hackathons/Virulence_AMR_Data_Index/master/Indexing_Figure.pdf)

Q: Should similarity/difference in sequence content correlate with similarity/difference in metadata?

A: Let's find out what it looks like currently!
![Metadata Pipeline](https://raw.githubusercontent.com/NCBI-Hackathons/Virulence_AMR_Data_Index/master/Metadata_accessor.png)

# Links

# Authors
Eric Holloway, Sergey Nurk, Brett E. Pickett, Ryan Connor	
