library(dplyr)
library(data.table)
#library(stringr)
#library(Biobase)

input_file <- "target_srr_metadata.csv"
target_srr_metadata <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)

input_file <- "amrfinder.csv"
amrfinder <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)
#split BioSampleID and ContigID
setDT(amrfinder)[, paste0("Contig_id", 1:2) := tstrsplit(Contig_id, "-")]
#merge 2 dataframes
combined = merge(target_srr_metadata, amrfinder, by.x="biosample", by.y="Contig_id1", all = TRUE)

input_file <- "files.csv"
files1 <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)
combined = merge(combined, files1, by.x="biosample", by.y="target_name", all = TRUE)

input_file <- "PDG000000098_all_isolates.csv"
PDG000000098_all_isolates <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)
combined$target_acc.y=NULL
#combined$sample_name=NULL
colnames(combined)[colnames(combined) == "target_acc.x"] <- "target_acc"
combined = merge(combined, PDG000000098_all_isolates, by.x="target_acc", by.y="target_acc", all = TRUE)

input_file <- "PDG000000098_cluster_list.csv"
PDG000000098_cluster_list <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)
colnames(PDG000000098_cluster_list) <- as.character(unlist(PDG000000098_cluster_list[1,]))
PDG000000098_cluster_list = PDG000000098_cluster_list[-1, ]
colnames(PDG000000098_cluster_list)[colnames(PDG000000098_cluster_list) == "target_acc"] <- "target_acc.y"
combined = merge(combined, PDG000000098_cluster_list, by.x=c("target_acc","biosample","PDS_acc"), by.y=c("target_acc.y","biosample_acc","PDS_acc"), all = TRUE)

input_file <- "PDG000000098_new_isolates.csv"
PDG000000098_new_isolates <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)
colnames(PDG000000098_new_isolates)[colnames(PDG000000098_new_isolates) == "target_acc"] <- "target_acc1"
combined = merge(combined, PDG000000098_new_isolates, by.x=c("target_acc","PDS_acc"), by.y=c("target_acc1","PDS_acc"), all = TRUE)

input_file <- "PDG000000098_SNP_distances.csv"
PDG000000098_SNP_distances <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)
combined = merge(combined, PDG000000098_SNP_distances, by.x=c("biosample","target_acc"), by.y=c("biosample_acc_1","target_acc_1"), all = TRUE)

#not informative
#input_file <- "PDG000000099_all_isolates.csv"
#PDG000000099_all_isolates <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)

#input_file <- "PDG000000099_cluster_list.csv"
#PDG000000099_cluster_list <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)

#input_file <- "PDG000000099_new_isolates.csv"
#PDG000000099_new_isolates <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)

#input_file <- "PDG000000099_SNP_distances.csv"
#PDG000000099_SNP_distances <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)
#combined = merge(combined, PDG000000099_SNP_distances, by.x="biosample", by.y="biosample_acc_1", all = TRUE)

input_file <- "references.csv"
references <- read.csv(input_file, header = TRUE, stringsAsFactors = FALSE)
combined = merge(combined, PDG000000099_SNP_distances, by.x="biosample", by.y="biosample_acc_1", all = TRUE)

#amrfinder1 <- str_split_fixed(amrfinder$Contig_id, "-", 2)
#amrfinder1 <- data.frame(amrfinder$Contig_id, do.call(rbind, amrfinder1))

#Z1 <- colnames(target_srr_metadata)
#Z2 <- colnames(amrfinder)
#Z3 <- colnames(files1)
#Z4 <- colnames(PDG000000098_all_isolates)
#Z5 <- colnames(PDG000000098_cluster_list)
#Z6 <- colnames(PDG000000098_new_isolates)
#Z7 <- colnames(PDG000000098_SNP_distances)
#Z8 <- colnames(PDG000000099_all_isolates)
#Z9 <- colnames(PDG000000099_cluster_list)
#Z10 <- colnames(PDG000000099_new_isolates)
#Z11 <- colnames(PDG000000099_SNP_distances)
#Z12 <- colnames(references)

#remove rows with N/A in ID columns
combined1 <- combined
combined1 <- combined1[rowSums(is.na(combined1[,c(1,2)]))==0,]

output <- "combined_bq_table.csv"
write.csv(combined1, file = output, row.names = FALSE)
