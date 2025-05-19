from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        NUM_LEN = len(words)

        # Use a variable to store last group added in answer array
        # Iterate through the array and pick the words alternately
        ans = [words[0]]
        curr_group = groups[0]

        for i in range(1, NUM_LEN):
            if groups[i] != curr_group:
                curr_group = groups[i]
                ans.append(words[i])
        return ans
