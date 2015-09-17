import urllib.request as urls
import re

data = """P04921_GLPC_HUMAN
A1TJ10
B3PYU7
B5FNU0
Q5PA87
P20268
A6LJ74
Q6A9W5
P01044_KNH1_BOVIN
Q4JAS3
P10153_RNKD_HUMAN
P00748_FA12_HUMAN
P19823_ITH2_HUMAN
C0Q5J8
"""

data = data.splitlines()
motif = re.compile(r'(?=(N[^P][ST][^P]))')
result = []
first = "http://www.uniprot.org/uniprot/"
for seq in data:
    check = seq
    response = urls.urlopen(first+check+".fasta")
    response = response.read()
    response = response.splitlines()[1:]

    for x in range(len(response)):
        response[x] = response[x].decode("utf-8")

    response = "".join(response)

    indexes = [str(m.start() + 1) for m in motif.finditer(response)]

    if indexes:
        result.append(seq)
        result.append(" ".join(indexes))


print("\n".join(result))
