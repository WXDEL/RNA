import sys
import numpy as np
import pandas as pd
#1.Input BLAST OUT6 & length of RNA
#makeblastdb -in THF.fasta -dbtype nucl -parse_seqids
#blastn -db THF.fasta -query c380n12motif.fasta -outfmt  "6 delim=@ qaccver saccver pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq" -out c380n12motifblast.out6 -num_threads 30  -word_size 5
r1_file_path = sys.argv[1]
#r1_file_path = 'c10277n12motifblast.out6'
RNAseq = int(sys.argv[2])
#RNAseq = 30 #length of RNA
data = pd.read_table(r1_file_path,sep='@',header=None,names=['qaccver', 'saccver', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore', 'qseq', 'sseq'])
data = pd.DataFrame(data)
#2. drop duplicates
data2=data.drop_duplicates(subset='qaccver')

line_num=data2.shape[0] #Rows of BLAST OUT
df0=pd.DataFrame(columns=['position','plus','minus','condition'])
numbers=list(range(1,RNAseq+1))
#3. calculate copy distribution
#campaign_ID_Sample1copy_sample2copy_...   
n=0 # count conditions
conditionsqaccver = data2.iloc[0,0]
conditions = conditionsqaccver.split('_')
while n <len(conditions)-2:
  n += 1
  count = 1 #count lines
  copy_total_plus = [0 for x in range(0,RNAseq)]
  copy_total_minus = [0 for x in range(0,RNAseq)]
  while count <= line_num:
      i = count-1
      blast_qaccver = 0
      blast_sstart = 0
      blast_send = 0
      blast_qseq = 0
      blast_sseq = 0
      blast_qaccver = data2.iloc[i,0]
      blast_sstart = data2.iloc[i,8]
      blast_send = data2.iloc[i,9]
      blast_qseq = data2.iloc[i,12]
      blast_sseq = data2.iloc[i,13]
      copy_num = blast_qaccver.split('_')
      #print(copy_num)
      if (blast_sstart-blast_send)<=0:
          blast_strand = 'plus'
          j = 0
          k = 0
          for nucl in blast_sseq:
              if (nucl != '-') and (nucl == blast_qseq[j]):
                  copy_posi=blast_sstart+k-1
                  copy_total_plus[copy_posi] += float(copy_num[n+1])
              elif (nucl == '-'):
                  k -= 1
              j += 1
              k += 1
      else:
          blast_strand = 'minus'
          j = 0
          k = 0
          for nucl in blast_sseq:
              if (nucl != '-') and (nucl == blast_qseq[j]):
                  copy_posi=blast_sstart-k-1
                  copy_total_minus[copy_posi] -= float(copy_num[n+1])
                  #print(copy_total_minus[copy_posi])
              elif (nucl == '-'):
                  k -= 1
              j += 1
              k += 1
      count += 1       
  df=pd.DataFrame({"position":numbers,"plus":copy_total_plus,"minus":copy_total_minus,"condition":[n for x in range(0,RNAseq)]})
  #print(df)
  #fileout='Condition_C' + str(n) + '_copy_position.csv'
  #df.to_csv(fileout)
  df0=pd.concat([df0,df])
fileout=r1_file_path + 'copy_position.csv'
df0.to_csv(fileout)
#'qaccver', 'saccver', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore', 'qseq', 'sseq'])
#  0          1          2         3         4            5          6        7        8         9      10        11           12      13  



