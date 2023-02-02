class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        maxLength = 1
        start = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > maxLength:
                            start = i
                            maxLength = j - i + 1
        return s[start : start + maxLength]

if __name__ == "__main__":
    test_cases = ["abba", "acdf", "aaaccaa", "acaca", "a", "aa"]
    solution = Solution()
    for s in test_cases:
        print(f'Longest palindromic subsequence of "{s}" is: {solution.longestPalindrome(s)}')