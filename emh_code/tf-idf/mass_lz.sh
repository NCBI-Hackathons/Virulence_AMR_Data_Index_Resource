#/bin/sh

for dna_file in `ls $1/* | grep -v dict`;
do
	python3 lzd_contig.py $dna_file &
done
