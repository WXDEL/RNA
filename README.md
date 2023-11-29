Motif pipeline for DEL Zipper in RNA affinity selection 

1. Motif in the UMI region
  Download "RNA.sh" and "Kmerout.py" into the same directory.

$./RNA.sh query db out RNAlen

  query: a query file, UMI seqs and copy count in fasta format.
  
  db: a db file: RNA seqs in fasta format.
  
  out: an output file of alignment.
  
  RNAlen: input the length of RNA in the db file.

  The final output is a "*copy_position.csv" file to draw pictures.

2. Motif in the coding region

  Download "BB_motif_script.R" and "c1174_1_10353_tag4_distribute.txt".
  Run "BB_motif_script.R" in R.
