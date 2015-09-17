def prob_dom(k, m, n):
    sum = k + m + n
    prob_homo = k/sum
    prob_hetero = m/sum
    prob_rec = n/sum
    prob_both_hetero = prob_hetero * (m-1)/(sum-1)
    prob_one_rec_w_hetero = 2 * prob_rec * (m/(sum-1))
    prob_both_rec = prob_rec * ((n-1)/(sum-1))
    print(1-(prob_both_rec + prob_one_rec_w_hetero * 0.5 + prob_both_hetero * 0.25))


#example
prob_dom(26, 29, 22)