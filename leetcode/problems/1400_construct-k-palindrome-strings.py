class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        # If the length of s is equal to k, then we can construct k strings with length 1
        if n == k:
            return True
        # If the length of s is less than k, then we can't construct k strings
        elif n < k:
            return False
        # Otherwise, the minium palindrome strings we can construct is the number of characters that have odd frequency
        else:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            return k >= sum([f & 1 for f in freq])
