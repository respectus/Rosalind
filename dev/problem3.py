def reverse_complement(seq):
    flip = list(seq[::-1])
    x = 0
    for base in flip:
        if base == 'A':
            flip[x] = 'T'
        if base == 'T':
            flip[x] = 'A'
        if base == 'G':
            flip[x] = 'C'
        if base == 'C':
            flip[x] = 'G'
        x += 1    
    print(''.join(flip))


example = "AAAACCCGGT"
dataset = "GACTCGATGTTGCTCAACTCAAGAGCGATGTACGTAGTCTCCTTTCTGATACGTACATCGTCGGCCTACGCGAGCCATTCACGTCTGGGTCGACTCTACCGGGGCGTTAATTCTTCCAAAGAAAATAGAGTTCCGTAAGACGCATTGGATTCTAAGCATCACTAAGCAATTGCGAGATAGGAGTCGCCATCACATTAGGCCCTTTCTCAGTGACCAGGGTGTCCCAAAAAGAACTTCAAATATTTCAGGAGTTTGAGGACATCATCGTCTCGACCGTCAGTCAGGGTCCGGACAATATATCCGGCACTCCGGCTGCCCAAGTAATACCCAGATGGCCCATTCACAGCTGAACTGGAGTGGCTCTCGAGCAGGAACTCTTCGAACCAACACCCATATATGATATAGCAGCTTGCCGATAAAAGTCTGGTGTCACGAAGGAGCGCCTAGAAGGTAACTCTTTTAGTAGCCTTCAGGGATAGCGCAGCCTACGATGAGTAAGGAATTAATCTCCCCTCTTGTGTTTGCAAGACTAAGCTCAAAAATGCAGCTTTGAAGACCACACTTTAATAGCGGTGTAACGGGAGACTAATCCCTGAGACGAACGCCTGACTAGTATGCTTAGAACGTTACGAGCAAGATTGACCAAACTAATTATGAAAATTAGCCCTCCGCTCTATGCCCTCATGTCACCACCGAACCGTCTTAACTCCAACCGAGTAAAGGCCCTCTATGGCCCCGGATACTTAAAATTGGGCGACAAGCCTAGAGGAACTATTCGTGCTGCAACCGCTGGTGTCTGAGAGTGGGTGCCGCTTGGTTCTTGTAAATTTTCCGTTATGCAGTACAGGGAGGCAATTGTATATCCTCTCCGACCACCAGTTATTGAATTTGAGGGACTTACGACCCCGTACGA"

reverse_complement(example)
reverse_complement(dataset)