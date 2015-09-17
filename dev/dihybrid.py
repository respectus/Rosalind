from scipy.misc import comb

with open('rosalind_lia.txt') as f:
    k, N = map(int, f.read().split())

prob = 0
for i in range(N, 2**k + 1):
    prob += comb(2**k, i) * ((0.25)**i) * ((0.75)**((2**k)-i))

print prob