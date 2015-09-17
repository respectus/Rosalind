def gc_content(seqs):
    # given: 10 dna_seqs in fasta format 
    # return: name /n content for highest gc content
    seq = [x.rstrip() for x in seqs]
    print(seq)
    dna_seqs = {seq[0][1:] : ''}
    gc_counts = {}
    last = ""
    for lines in seq:
        if lines[0] == '>':
            last = lines[1:]
            dna_seqs.setdefault(last, '')
        else:
            dna_seqs[last] += lines
    for name, seq in dna_seqs.items():
        gc_counts.setdefault(name, 100 * (seq.count('G') + seq.count('C'))/len(seq))
    print(gc_counts) 
    max = 0
    max_key = ""
    for name in gc_counts:
        if gc_counts[name] > max:
            max = gc_counts[name]
            max_key = name
    print(max_key)
    print(max)



with open('rosalind_gc.txt') as f:
    content =f.readlines()
    gc_content(content)