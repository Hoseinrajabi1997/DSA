def longest_palindromic_subsequence(s):
    i = 0
    j = len(s) - 1
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return longest_palindrom(s, i, j, dp)


def longest_palindrom(s, i, j, dp):
    if i == j:
        return 1

    if i > j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if s[i] == s[j]:
        dp[i][j] = 2 + longest_palindrom(s, i + 1, j - 1, dp)
        return dp[i][j]

    dp[i][j] = max(longest_palindrom(s, i + 1, j, dp), longest_palindrom(s, i, j - 1, dp))
    return dp[i][j]


if __name__ == '__main__':
    s = "abcsdsa"
    print(" LCS = ", longest_palindromic_subsequence(s))