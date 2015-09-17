def overlapping(dna, k):
    for x in range(len(dna)):
        match = re.compile(r"^%s" % str(dna[x][1][-k:]))
        for y in range(len(dna)):
            if x !=y:
                if match.match(dna[y][1]):
                    print(dna[x][0]+ dna[y][0]])



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
    print(dna_seqs)
    return dna_seqs

with open('example.txt') as f:
    content =f.readlines()
    dnas = list(fasta_to_dict(content).values())
    overlapping(dnas, 3)

with open('rosalind_cons.txt') as f:
    content =f.readlines()
    dnas = list(fasta_to_dict(content).values())
    overlapping(dnas, 3)