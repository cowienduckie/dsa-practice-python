class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        max_len = float("-inf")

        for l in range(n):
            for r in range(l + 1, n):
                curr_len = r - l + 1
                sub_str = s[l : r + 1]
                rev_str = sub_str[::-1]

                if sub_str == rev_str and curr_len > max_len:
                    ans = sub_str
                    max_len = curr_len

        return ans


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n, max_len = len(s), 1
        ans = s[0]

        def expand_around_center(l: int, r: int) -> None:
            nonlocal max_len, ans
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    ans = s[l : r + 1]
                l -= 1
                r += 1

        for i in range(n - 1):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)

        return ans
