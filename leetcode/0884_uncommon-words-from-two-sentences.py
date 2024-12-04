from typing import Dict, List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Use a dictionary to store each word's occurrences in both sentences
        word_dict: Dict[str, List[int]] = {}

        for w in s1.split(" "):
            if w not in word_dict:
                word_dict[w] = [1, 0]
            else:
                word_dict[w][0] += 1

        for w in s2.split(" "):
            if w not in word_dict:
                word_dict[w] = [0, 1]
            else:
                word_dict[w][1] += 1

        # Loop through the dict's values to find which word is uncommon
        ans = []
        for word, occurrences in word_dict.items():
            if occurrences[0] + occurrences[1] == 1:
                ans.append(word)

        return ans
