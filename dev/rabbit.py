def rabbits(n, k):
    mate_pairs = 1
    if n == 1:
        return 1
    elif n == 2:
        return 1 
    elif n == 3:
       return 1 + k
    else:
        return rabbits(n-1, k) + rabbits(n-2,k)*k 


#example
rabbits(5, 3)

#dataset
rabbits(31, 4)

