class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = len(searchWord)
        for idx, word in enumerate(sentence.split()):
            if len(word) >= l and word[:l] == searchWord:
                return idx + 1
        return -1
