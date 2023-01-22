def longest_palindromic_subsequence(s):
    length = len(s)
    dp = [[0] * length for _ in range(length)]
    for i in range(length):
        dp[i][i] = 1 # every single char is a palindrome of length 1

    for start in range(length - 1, -1, -1):
        for end in range(start + 1, length):
            if s[start] == s[end]:
                dp[start][end] = 2 + dp[start + 1][end - 1]
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
    return dp[0][length - 1]


if __name__ == "__main__":
    test_cases = ["abcdz", "bcfd", "aaaabcaa", "bbbab", "abacdfgdcaba", "abacdfgdcabba"]
    for s in test_cases:
        print(f'Longest palindromic subsequence of "{s}" is: {longest_palindromic_subsequence(s)}')