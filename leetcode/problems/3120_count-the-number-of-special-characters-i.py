class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26

        for c in word:
            if ord(c) < ord("a"):
                upper[ord(c) - ord("A")] = True
            else:
                lower[ord(c) - ord("a")] = True

        return sum(1 if lower[i] and upper[i] else 0 for i in range(26))
