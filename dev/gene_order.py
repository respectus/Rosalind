import sys
import itertools

data = int(sys.argv[1])
result = [x for x in itertools.permutations([x for x in range(1,data+1)])]
for i in range(len(result)):
    result[i] = [str(x) for x in result[i]]
    result[i] = " ".join(result[i])

print(len(result))
print("\n".join(result))