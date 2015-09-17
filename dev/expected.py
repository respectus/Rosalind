def expected(number):
    population = sum(2*x for x in number)
    one = 2 * number[0]
    two = 2 * number[1]
    three = 2 *number[2]
    four = 2 * 0.75 * number[3]
    five = 2 * 0.5 * number[4]
    print((one+two+three+four+five))

example = "18657 19080 17592 19260 16888 16607"
expected([int(x) for x in example.split(' ')])