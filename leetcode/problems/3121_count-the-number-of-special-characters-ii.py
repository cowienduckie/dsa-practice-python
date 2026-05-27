class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26
        valid = [True] * 26

        for c in word:
            if ord(c) < ord("a"):
                upper[ord(c) - ord("A")] = True
            else:
                i = ord(c) - ord("a")
                lower[i] = True
                valid[i] = not upper[i]

        return sum(1 if lower[i] and upper[i] and valid[i] else 0 for i in range(26))
