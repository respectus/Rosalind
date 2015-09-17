def mortal_rabbits(n, m):
    fibs = []
    for month in range(n):
        if month < m:
            if month == 0 or month == 1:
                fibs.append(1)
            else:
                fibs.append(fibs[-1] + fibs[-2])
        else:
            total = 0
            for x in range(month - m, month - 1):
                total += fibs[x]
            fibs.append(total)
    print(fibs[-1])

#example
mortal_rabbits(94, 18)

