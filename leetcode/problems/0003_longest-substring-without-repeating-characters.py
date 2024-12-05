class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            # Base case -> Empty string
            return 0

        # Use a dictionary to store last index of each character
        # Use a prefix array to store the longest substring ending at each index
        last_index = {s[0]: 0}
        max_substr = [1] * n
        ans = 1

        for i in range(1, n):
            if s[i] in last_index:
                # If the character s[i] is already existed, there are two cases and we choose the smaller one:
                # 1. s[i] will be included in the new substring from the last occurrence of s[i] + 1 to i
                # 2. s[i] will lengthen the previous substring by 1
                max_substr[i] = min(max_substr[i - 1] + 1, i - last_index[s[i]])
            else:
                # If the character s[i] is new, lengthen the previous substring by 1
                max_substr[i] = max_substr[i - 1] + 1

            last_index[s[i]] = i
            ans = max(ans, max_substr[i])
        return ans


class Solution2:
    """
    Optimized version using sliding window but the same idea when meeting existing characters
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        n, l, ans = len(s), 0, 0
        last_index = dict()

        for r in range(n):
            if s[r] in last_index and last_index[s[r]] >= l:
                # If the character s[r] is already existed, and the last occurrence is in the current window
                # Move the left pointer to the right of the last occurrence of s[r]
                l = last_index[s[r]] + 1
            else:
                # If the character s[r] is new, update the answer
                ans = max(ans, r - l + 1)
            last_index[s[r]] = r
        return ans
