class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        letters = []
        i1 = i2 = 0

        while i1 < len(word1) and i2 < len(word2):
            letters.append(word1[i1])
            letters.append(word2[i2])
            i1 += 1
            i2 += 1

        while i1 < len(word1):
            letters.append(word1[i1])
            i1 += 1

        while i2 < len(word2):
            letters.append(word2[i2])
            i2 += 1

        return "".join(letters)
