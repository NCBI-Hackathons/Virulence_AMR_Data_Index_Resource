cf = open('all_contigs.txt')
contigs = {}
for line in cf.readlines():
    srrA, srrB, ncd_txt, _, _, _, _, _, _ = line.strip().split('\t')
    contigs[(srrA, srrB)] = float(ncd_txt)
cf.close()

cm = open('all_meta.txt')
meta = {}
for line in cm.readlines():
    srrA, srrB, ncd_txt, _, _, _, _, _, _ = line.strip().split('\t')
    meta[(srrA, srrB)] = float(ncd_txt)
cm.close()

f = open('all_meta_contigs_ncd.txt', 'w')
for k in contigs.keys():
    f.write(" ".join(k) + " ")
    f.write(str(contigs[k]) + " ")
    f.write(str(meta[k]) + "\n")
f.close()
