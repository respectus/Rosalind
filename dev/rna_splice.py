import sys
from rosalind_helper import dna2_protein

#data = sys.argv[1].split()
data = """>Rosalind_1106
ATGAAGGGGGCTATCTATAGCCGCTATAAGACGAGCGGACGGGTTCGCTCAGGGGGGTAC
TCTACACGCTGTCGCAAGTACCCATAAGCTATTTATTTCTTTATTAAGTGGTAAGTCGGG
GCGATCAAGTTGGCAATCTACACCGGATCTAGCAGGCTAGGTCGTCTCGCTACTGGTCGC
CATCGTCACAAACGTGTCTATCCCTACCTCAGAGCGCTGGTTTTGTTTCAGACCGGCCAC
GCCGTTCCTTTGAAATCAAACTGAATAGGTTCAGCATAGAGTTGATTCAGGGGGCTTACG
GCGACGACTGTTGCGCAAAGGCACTGGAAGGGTAGGGAGAACCTGAAAAGGTTTCTTGCC
CATAGTAACTCAAGCTATCAACGTAGAGCCTGTGGTTCAACTCCGCATAAATTGATAGGC
CACACATGTTATACTTGCCGACGTCTTATGACGGAAGGTCGGGAATCATGAGCTGGAAGC
CCACGATCGGAAACGACAACGCGAGCTCCTTCCACAGTGCGTGAATCAGCAATGGGCAGA
CAAGTCACGAACACGTACATTGTCCTAGGGACCGCCTGGTTTTCCCTGTGATGTTTTGTA
TCCTTGAACATTATATGCCTGTGGTTGGAACACAATATATCCATTATGAAGAAACGGCTC
AGTGTTATCGAATCAGGCATAAGATGTACAGACTACCGCACAATATCAGGCTGTACGGGG
GGTAGTGATCTCCAACACAACACATCTACTCATTTTTGCCGTCGTTTAAAAAGACCTACT
CAGTGGCGTTAGTCTCAGCTTAATCTTCTTGGAGGTGTCCCAAACCAGGAGAGCATTGGA
AAGGAGTTCAACCGGATTGCCATGTTTTATGCATGTTCACTCGAATGACCGTCTTCCGTG
ACAAGCCAGCTGTGGTCGTTTCTGCACGACCTTATAGACCAGTTCGCACAATTACGAACA
TTGTCCCACGTTGA
>Rosalind_8698
AGACCTACTCAGTGGCGTTAGTCTCAGCTTAATCTTCTTGGAGGTGTC
>Rosalind_6243
TCACAAACGTGTCTATCCCTACCTCAGAGCGCTGGT
>Rosalind_2259
TCAAGTTGGCAATCTACACCGGATCTAGCAGGCTAGGTCG
>Rosalind_3754
CGCTCAGGGGGGTACTCTACACGCTGTCGCAAGTACCCATAAGCTATTT
>Rosalind_1725
AAACTGAATAGGTTCAGCATAGAGTTGATTCAGG
>Rosalind_9834
GTGATGTTTTGTATCC
>Rosalind_0862
GAATCATGAGCTGGAAGCCCACGATCGG
>Rosalind_5486
GCGCAAAGGCACTGGAAGGGTAGGGAG
>Rosalind_0285
CTCCAACACAACACA
>Rosalind_2367
TGTGGTTCAACTCCGCATAAATTGATA
>Rosalind_8807
CAGCAATGGGCAGACAAGTCACGAACACGTACATTGTCCT
>Rosalind_0149
TGTTCACTCGAATGACCGTCTTCCGTGACAAGCCAGCT
>Rosalind_3474
ATGAAGAAACGGCTCAGTGTTATC"""
data = data.split()
original = ""
data.pop(0)
count = 0
for x in range(len(data)):
    if data[x][0] == '>':
        data.pop(x)
        break
    else:
        count += 1
        original += data[x]
for x in range(count):
    data.pop(0)
introns = []
next = ""
for x in range(len(data)):
    if data[x][0] == '>':
        introns.append(next)
        next = ""
    else:
        next += data[x]
introns.append(next)
for intron in introns:
    original = original.replace(intron, "")
print(dna2_protein(original))



