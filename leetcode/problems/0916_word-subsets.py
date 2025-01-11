from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Find the maximum frequency of each letter in words2
        max_freq = [0] * 26
        for word in words2:
            word_freq = self.split_word(word)
            for i in range(26):
                max_freq[i] = max(max_freq[i], word_freq[i])

        # Check if each word in words1 is a "universal" word, which mean all word in words2 is a subset of it
        ans = []
        for word in words1:
            word_freq = self.split_word(word)
            if all([wf >= mf for wf, mf in zip(word_freq, max_freq)]):
                ans.append(word)
        return ans

    def split_word(self, word: str) -> List[int]:
        """
        Split the word into a list of frequencies of each letter
        """
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord("a")] += 1
        return freq
