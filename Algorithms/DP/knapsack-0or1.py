def knap_sack(profits, profits_length, weights, capacity):
    knap_sack_track = [[ -1 for i in range(capacity+1)] for j in range(profits_length+1)]
    result = knap_sack_rec(profits, profits_length, weights, capacity, knap_sack_track, 0)
    return result

def knap_sack_rec(profits, profits_length, weights, capacity, track, index):

    if index >= profits_length:
        return 0
    
    if track[index][capacity] != -1:
        return track[index][capacity]
    profit_include = 0
    if weights[index] <= capacity:
        profit_include = profits[index] + knap_sack_rec(profits, profits_length, weights, capacity - weights[index], track, index+1)

    profit_exclude = knap_sack_rec(profits, profits_length, weights, capacity, track, index+1)

    track[index][capacity] = max(profit_include, profit_exclude)

    return track[index][capacity]

if __name__ == '__main__':
    profits = [10, 60, 40, 80]  
    weights = [1, 2, 3, 5] 
    print("Max Profit = ", knap_sack(profits, len(profits), weights, 7))
    print("Max Profit = ", knap_sack(profits, len(profits), weights, 6))
