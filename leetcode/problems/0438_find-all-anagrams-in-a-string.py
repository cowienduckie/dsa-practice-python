from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Base case
        p_len, s_len = len(p), len(s)
        if p_len > s_len:
            return []

        # Count occurrences of every letters in p and some first letters in s
        p_count = [0] * 26
        s_count = [0] * 26
        for i in range(p_len):
            p_count[ord(p[i]) - ord("a")] += 1
            s_count[ord(s[i]) - ord("a")] += 1

        # Using sliding window to check every p-length substrings in s
        def is_anagram() -> bool:
            for i in range(26):
                if s_count[i] != p_count[i]:
                    return False
            return True

        ans = []
        if is_anagram():
            ans.append(0)

        for i in range(p_len, s_len):
            s_count[ord(s[i]) - ord("a")] += 1
            s_count[ord(s[i - p_len]) - ord("a")] -= 1
            if is_anagram():
                ans.append(i - p_len + 1)

        return ans
