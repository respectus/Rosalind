import re

# simplified regex
def find_motif(seq):
    s = seq[0]
    t = seq[1]
    positions = [str(motif.start() + 1) for motif in re.finditer('(?=%s)' % t, s)]
    print(' '.join(positions))

#example
find_motif(("GATATATGCATATACTT", "ATAT"))

with open('rosalind_subs.txt') as f:
    input = f.readlines()
    find_motif((input[0].rstrip(), input[1].rstrip()))
