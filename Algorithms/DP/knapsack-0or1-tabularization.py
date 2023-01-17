def knap_sack(profits, profits_length, weights, capacity):

    knap_sack_track = [[ -1 for i in range(capacity+1)] for j in range(profits_length+1)]


    for i in range(profits_length + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                knap_sack_track[i][j] = 0
            elif weights[i-1] <= j:
                knap_sack_track[i][j] = max(profits[i-1] + knap_sack_track[i - 1][j - weights[i - 1]],
                                         knap_sack_track[i - 1][j])
            else:
                knap_sack_track[i][j] = knap_sack_track[i - 1][j]

    return knap_sack_track[profits_length][capacity]








if __name__ == '__main__':
    profits = [10, 60, 40, 80] 
    weights = [1, 2, 3, 5]
    print("Max Profit = ", knap_sack(profits, len(profits), weights, 7))
    print("Max Profit = ", knap_sack(profits, len(profits), weights, 6))