import itertools
from rosalind_helper import tuples_to_spaces
data = """O G N X K Y P B I Q
2
"""
data = data.split() 
length = int(data.pop())
result = [x for x in itertools.product(data, repeat=length)]
print("\n".join(tuples_to_spaces(result, "")))
