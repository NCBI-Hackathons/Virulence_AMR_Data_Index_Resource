f = open('GCA_000407325.1_Ente_faec_Efm_NY2-2_V2_genomic.gff')

info = []
accession = None
key = 'product'
for line in f.readlines():
    if key in line:
        common_fields = line.strip().split("\t")
        if not accession:
            accession = common_fields[0]
        custom_fields = common_fields[-1].split(";")
        select_keyvar = [field for field in custom_fields if key in field][0]
        print(accession,"\t",select_keyvar.split("=")[1])
