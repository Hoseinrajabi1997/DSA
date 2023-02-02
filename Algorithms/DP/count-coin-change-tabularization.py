def count_change(denoms, denoms_length, amount):
    """
    Finds the number of ways that the given number of cents can be represented.
    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """

    # Edge cases
    if amount <= 0 or denoms_length <= 0:
        return 0

    # We need n+1 rows as the table
    # is constructed in bottom up
    # manner using the base case 0
    # value case (n = 0)

    lookup_table = [[0 for x in range(denoms_length)] for x in range(amount + 1)]

    # Fill the enteries for 0
    # value case (n = 0)
    for i in range(denoms_length):
        lookup_table[0][i] = 1

    # Fill rest of the table entries
    # in bottom up manner
    for i in range(1, amount + 1):
        for j in range(denoms_length):

            # Count of solutions including denoms[j]
            x = lookup_table[i - denoms[j]][j] if i - denoms[j] >= 0 else 0

            # Count of solutions excluding denoms[j]
            y = lookup_table[i][j - 1] if j >= 1 else 0

            # Total count
            lookup_table[i][j] = x + y
    for i in lookup_table:
        print(i)
    return lookup_table[amount][denoms_length - 1]


# Driver code to test the above function
if __name__ == '__main__':

    denoms = [25, 2,3, 5, 1]
    print(count_change(denoms, len(denoms), 10))