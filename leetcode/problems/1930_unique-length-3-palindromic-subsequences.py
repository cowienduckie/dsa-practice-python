class Solution:
    """
    Solution with time complexity O(n^2)
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        # For each letter in the string, we only need to consider first and last occurrence
        # Update the answer by the number of unique characters between those occurrences exclusively
        ans = 0
        checked = [False] * 26
        for i in range(n):
            # Skip if the current character has been checked
            if checked[ord(s[i]) - ord("a")]:
                continue
            checked[ord(s[i]) - ord("a")] = True
            # Find the last occurrence of the current character
            for j in range(n - 1, i + 1, -1):
                if s[i] == s[j]:
                    char_set = set(s[i + 1 : j])
                    ans += len(char_set)
                    break
        return ans


class Solution:
    """
    Solution with optimized time complexity O(n)
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        # Use a array to store all occurrences of each letter
        indices = [[] for _ in range(26)]
        for i in range(n):
            indices[ord(s[i]) - ord("a")].append(i)

        # For each letter in the string, we only need to consider first and last occurrence
        # Update the answer by the number of unique characters between those occurrences exclusively
        ans = 0
        for i in range(26):
            if len(indices[i]) < 2:
                continue
            first, last = indices[i][0], indices[i][-1]
            ans += len(set(s[first + 1 : last]))

        return ans
