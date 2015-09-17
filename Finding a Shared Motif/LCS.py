def fasta_to_dict(dna_fasta):
    seq = [x.rstrip() for x in dna_fasta]
    dna_seqs = {seq[0][1:] : ''}
    last = ""
    for lines in seq:
        if lines[0] == '>':
            last = lines[1:]
            dna_seqs.setdefault(last, '')
        else:
            dna_seqs[last] += lines
    return dna_seqs

def lcsubstring(collection):
    largest = ''
    for x in range(len(collection[0])):
        for y in range(len(collection[0]) - x + 1):
            if y > len(largest) and all(collection[0][x:x+y] in dna for dna in collection):
                largest = collection[0][x:x+y]
    return largest


with open('rosalind_lcsm.txt') as f:
    content =f.readlines()
    dnas = list(fasta_to_dict(content).values())
    lcsubstring(dnas)
