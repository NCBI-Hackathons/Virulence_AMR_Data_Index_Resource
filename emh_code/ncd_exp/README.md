In order to reproduce the comparison you'll need the directory `ncd_shuffle_base` and the script `mass_exp.sh`.  You will also need to pip install `pandas`.

In the `mass_exp.sh` file it runs through a sequence of numbers creating new experiment directories copied from `ncd_shuffle_base` and naming each new directory with the sequence number as suffix.  It then starts a background process running the `forever.sh` script which runs the Python script and restarts it if it fails.  The Python scripts downloads the necessary files from the Google Cloud bucket into base directory `data`.  If the file has already been downloaded into `data` then the script will use the local file.  The files are preprocessed, and then compared using the normalized compression distance.  The results are written to files `meta_<id num>.txt` and `contigs_<id num>.txt`.  The id numbers are picked randomly to avoid overwritting results if the Python scripts fail and have to be restarted.

The reason why many experiment directories are used is because Python only seems to use two cores regardless of the number of sub processes.  So, to use more than two cores, multiple Python jobs have to be started.  Recommendation is to modify the sequence range in `mass_exp.sh` to generate enough experiment Python jobs to maximize CPU utilization across all cores.

Results can be collected with the following commands:
```
cat ncd*/contigs*.txt | sort | uniq > all_contigs.txt
cat ncd*/meta*.txt | sort | uniq > all_meta.txt
```

The script `process_raw_results.py` will combine the meta and contig NCD results into a single file so they can be compared.
The following commands will combine the results and then visualize them with an R scatterplot.
```
python process_raw_results.py
# Inside R repl
mc <- read.table('all_meta_contigs_ncd.txt')
plot(mc[,3], mc[,4])
```

## Synthetic Results
In the `emh_code` directory there is a `preprocess.py` script that generates synthetic data.  It creates two groups of metadata and contig synthetic data strings.  Each group has two strings for a total of four strings for metadata and four strings for contigs.  

Each group has a unique distribution for generating the data strings, so all the strings from the same group should be closer to each other by the NCD metric, and when comparing strings between different groups the strings will be farther.

To run NCD metric with synthetic data, run the following command from the `emh_code` directory.
```
python3 master.py
```
This will generate meta and contigs comparison files comparing four different metadata strings and four different contig strings.  The files should show that strings 1 and 2 are close and strings 3 and 4 are close, and all other pairwise comparisons are more distant.
