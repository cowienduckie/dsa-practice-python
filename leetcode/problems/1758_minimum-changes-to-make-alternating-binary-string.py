class Solution:
    def minOperations(self, s: str) -> int:
        # Track operations needed if final string starting with 0 and 1
        s0 = s1 = 0
        for i in range(len(s)):
            if i & 1:
                s0 += 1 if s[i] == '0' else 0
                s1 += 1 if s[i] == '1' else 0
            else:
                s0 += 1 if s[i] == '1' else 0
                s1 += 1 if s[i] == '0' else 0
        return min(s0, s1)