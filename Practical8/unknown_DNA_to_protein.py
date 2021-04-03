
import os
import re

os.chdir('D:/IBI1_2020-21/Practical8')
codon_table={'ATA':'J', 'ATC':'I', 'ATT':'I', 'ATG':'M',
             'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
             'AAC':'B', 'AAT':'N', 'AAA':'K', 'AAG':'K',
             'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
             'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
             'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
             'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Z',
             'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
             'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
             'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
             'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
             'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
             'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
             'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
             'TAC':'Y', 'TAT':'Y', 'TAA':'O', 'TAG':'U',
             'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W'}

allcdna=input('enter the file name:')
genes=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output=open(allcdna)
for line in allcdna:
    if 'unknown function' in line:
        print(re.search(r'gene:(\w+)',line).group()) #search unknown function genes and list them
        line=allcdna.readline() #change to next line to read the sequence
        geneseq=''
        protein=''
        while '>' not in line:
            geneseq=str(geneseq)+str(line) #add all sequence of this unknown function gene
            geneseq=re.findall(r'[A-Z]',geneseq) #Remove newline characters
            result=''
            for item in geneseq:
                result=result+item #consolidate the sequence into a single string
            for i in range(0,len(geneseq),3):
                codon=result[i:i+3]
                protein=protein+codon_table[codon]    
            line=allcdna.readline() #change to next unknown function gene
        print('coded protein:'+str(protein))