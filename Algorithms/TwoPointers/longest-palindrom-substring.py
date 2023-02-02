class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > max_len:
                    res=s[left:right+1]
                    max_len = right - left + 1
                left -= 1
                right += 1
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > max_len:
                    res=s[left:right+1]
                    max_len = right - left + 1
                left -= 1
                right += 1
        return res

    
if __name__ == "__main__":
    test_cases = ["abba", "acdf", "aaaccaa", "acaca", "a", "aa"]
    solution = Solution()
    for s in test_cases:
        print(f'Longest palindromic subsequence of "{s}" is: {solution.longestPalindrome(s)}')