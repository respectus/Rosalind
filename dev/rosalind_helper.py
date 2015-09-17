
def reverse_complement(strand):
    result = ""
    for base in strand:
        if base == 'A':
            result += 'T'
        elif base == 'G'
            result += 'C'
        elif base == 'C'
            result += 'G'
        elif base += 'T'
            result += 'A'
        else:
            raise ValueError
    return result[::-1]

def tuples_to_spaces(results):
    for i in range(len(results)):
        results[i] = [str(x) for x in results[i]]
        results[i] = " ".join(results[i])
    return results

def mass_table():
    result = {'T': 101.04768, 'E': 129.04259, 'P': 97.05276, 'W': 186.07931, 'Q': 128.05858, 'S': 87.03203, 'N': 114.04293, 'Y': 163.06333, 'H': 137.05891, 'R': 156.10111, 'F': 147.06841, 'D': 115.02694, 'A': 71.03711, 'C': 103.00919, 'I': 113.08406, 'G': 57.02146, 'V': 99.06841, 'K': 128.09496, 'M': 131.04049, 'L': 113.08406}
    return result

def dna_table():
    return {'GCT': 'A', 'ACA': 'T', 'TTT': 'F', 'CGC': 'R', 'TGT': 'C', 'TGG': 'W', 'GTA': 'V', 'GTT': 'V', 'TCA': 'S', 'CAG': 'Q', 'CTA': 'L', 'GAC': 'D', 'AAT': 'N', 'CCT': 'P', 'CCG': 'P', 'GAT': 'D', 'TTC': 'F', 'GCG': 'A', 'ATA': 'I', 'ACG': 'T', 'TAT': 'Y', 'GTG': 'V', 'TCC': 'S', 'GCA': 'A', 'TCG': 'S', 'ATG': 'M', 'GGT': 'G', 'TAA': 'Stop', 'GGG': 'G', 'AAC': 'N', 'CAA': 'Q', 'AGT': 'S', 'TTG': 'L', 'ATT': 'I', 'ACC': 'T', 'CTT': 'L', 'GCC': 'A', 'AGA': 'R', 'GGC': 'G', 'GGA': 'G', 'AAG': 'K', 'CGA': 'R', 'GAA': 'E', 'TTA': 'L', 'ACT': 'T', 'CGG': 'R', 'AAA': 'K', 'CTC': 'L', 'CGT': 'R', 'CCC': 'P', 'TCT': 'S', 'CAC': 'H', 'TAG': 'Stop', 'ATC': 'I', 'CAT': 'H', 'TAC': 'Y', 'AGG': 'R', 'TGA': 'Stop', 'GAG': 'E', 'CCA': 'P', 'GTC': 'V', 'TGC': 'C', 'AGC': 'S', 'CTG': 'L'}

def rna_table():
    return {'CUC': 'L', 'UAG': 'Stop', 'ACA': 'T', 'AUA': 'I', 'UGA': 'Stop', 'CGC': 'R', 'GCU': 'A', 'GGG': 'G', 'GUC': 'V', 'UAA': 'Stop', 'CAG': 'Q', 'UUU': 'F', 'GAC': 'D', 'CGU': 'R', 'GAA': 'E', 'UCG': 'S', 'AAG': 'K', 'UGU': 'C', 'GUG': 'V', 'CAA': 'Q', 'CCG': 'P', 'AGC': 'S', 'UGC': 'C', 'AGU': 'S', 'UCU': 'S', 'GCG': 'A', 'GAU': 'D', 'ACG': 'T', 'UAU': 'Y', 'AGG': 'R', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'AAC': 'N', 'CCU': 'P', 'UUA': 'L', 'GCA': 'A', 'ACC': 'T', 'CGA': 'R', 'UUC': 'F', 'CUA': 'L', 'GGC': 'G', 'GUA': 'V', 'AUC': 'I', 'UAC': 'Y', 'GCC': 'A', 'ACU': 'T', 'AAA': 'K', 'CUU': 'L', 'GGA': 'G', 'CGG': 'R', 'CCC': 'P', 'CAU': 'H', 'CAC': 'H', 'UCA': 'S', 'GGU': 'G', 'AAU': 'N', 'UGG': 'W', 'GAG': 'E', 'CCA': 'P', 'AGA': 'R', 'UCC': 'S', 'GUU': 'V', 'AUU': 'I'}

def rna_table_nums():
    return {'F' : 2, 'L': 6, 'S': 6, 'Y': 2, 'Stop': 3, 'C': 2, 'W': 1,
                'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2,
                'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4}