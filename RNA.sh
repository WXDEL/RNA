query=$1
db=$2
out=$3
RNAlen=$4
makeblastdb -in ${db} -dbtype nucl -parse_seqids

blastn -db ${db} -query ${query} -outfmt  "6 delim=@ qaccver saccver pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq" -out ${out} -num_threads 30  -word_size 5

python ./Kmerout.py ${out} ${RNAlen}

