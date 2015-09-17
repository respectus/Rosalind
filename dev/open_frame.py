import re
from rosalind_helper import dna_strand2
motif = re.compile(r'(?=(ATG))')

data = """CACCGGCTTTGACAGCGTCTTCGCAATCCCTTCAATGAAGCTAGCGTTGGTCGGGAACAA
GGGTCCAGTTAAGAGCCGGGGATCTCGGTCGCGAACAATTCGTCCATTCTAAACAGCCTG
TTCCATCGCGTATCAATCTTGCCCTTGCTTTAGCACGATCTGCGATCGATCATACATTCA
CTGTTGCAATCTTACGTCAGTGAATCTTTCCCAACGAGGGGTGAACTACGCGAACTACAC
CAGACCAAAACGCCTTCTACCGCAACTGTCTAAGACTATTGTTTCACACTCTGGGTCCAC
CCTGTTAAAGATGTAGCCTCCCTTTTGATTGGCTCGCGGATGGAGGCGCCTTCTCAAACT
AGGCTCTTGTTAGATACAGGTTCCTCGTCGGCTCGTCTCCAGGCAGCGCATTCCACAAAC
TCACCCTAGCCGTCATGGGCGTAACTTTCTCCTAGCTAGGAGAAAGTTACGCCCATGGTC
GGATATTACGCCTCTGAGTCGTAGTGCGTGGTTCCTTCACTACACAGAGCGAATTAGAAC
CTAACAATGAAAGATTCCATAGCGCCGTCATAGACCAAGCACATATTCCAACTTTCGGGC
GATTAACTACGCTTGGTGACCCCTTACGTACCACGGGCTGAATTGCCTAACGGGGGGCCG
GTCCATTGCCCAGCCTCTAACGATTAAGCCTGGGCATGCTTGGGCGCCGCCCTGTCGTAC
TCGTCATAATGCGAGAAAAGTCTACGCCTCAGCGCGGCTCGCTGGTATTTCAGGAACAGA
TTAAGTACCCCTTAGGTTTCGGGCAGTGCCCGAGGAACTGACCATCATATCAACGTAACG
CGCTTGTCTCTATCGTTGATCGATGGAGTTGCTGACGCGACACATCGCGAATTTGCGCAG
GAAACCGTTA"""
data = "".join(data.split())
data1 = dna_strand2(data)

dna_table = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G """

dna_table = dna_table.split()
translate = {}
for x in range(0,len(dna_table),2):
    translate[dna_table[x]] = dna_table[x+1]
indexes = [m.start() for m in motif.finditer(data)]
indexes2 = [m.start() for m in motif.finditer(data1)]
result = []
for index in indexes:
    next = data[index:index+3]
    cur = index + 3
    protein = ""
    while next!="" and translate[next] != 'Stop':
        protein += translate[next]
        next = data[cur:cur+3]
        cur += 3
    if next != "":
        result.append(protein)

for index in indexes2:
    next = data1[index:index+3]
    cur = index + 3
    protein = ""
    while next != "" and translate[next] != 'Stop':
        protein += translate[next]
        next = data1[cur:cur+3]
        cur += 3
    if next != "":
        result.append(protein)

print("\n".join(set(result)))

