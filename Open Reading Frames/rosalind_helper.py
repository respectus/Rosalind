
def dna_strand2(strand):
    result = ""
    for base in strand:
        if base == 'A':
            result += 'T'
        elif base == 'G':
            result += 'C'
        elif base == 'C':
            result += 'G'
        else:
            result += 'A'
    return result[::-1]
    