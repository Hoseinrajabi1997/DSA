def count_change(denoms, denoms_length, amount):
    dp = [[-1 for _ in range(amount + 1)] for _ in range(denoms_length + 1)]
    return count_change_recursive(denoms, denoms_length, amount, dp)

def count_change_recursive(denoms, denoms_length, amount, dp):
    if amount == 0:
        return 1
    if denoms_length == 0:
        return 0
    if dp[denoms_length][amount] != -1:
        return dp[denoms_length][amount]
    if denoms[denoms_length-1] > amount:
        dp[denoms_length][amount] = count_change_recursive(denoms, denoms_length-1, amount, dp)
    else:
        dp[denoms_length][amount] = count_change_recursive(denoms, denoms_length, amount - denoms[denoms_length-1], dp) + count_change_recursive(denoms, denoms_length-1, amount, dp)
    return dp[denoms_length][amount]

if __name__ == "__main__":
    denoms = [1, 2, 3]
    denoms_length = len(denoms)
    amount = 4
    print(count_change(denoms, denoms_length, amount)) # should return 4
    denoms = [2, 5, 3, 6]
    denoms_length = len(denoms)
    amount = 10
    print(count_change(denoms, denoms_length, amount)) # should return 5