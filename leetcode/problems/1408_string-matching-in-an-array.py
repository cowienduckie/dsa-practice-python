from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []
        words.sort(key=lambda x: len(x))
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans


class Solution:
    """
    Pythonic solution
    """

    def stringMatching(self, words: List[str]) -> List[str]:
        combine = " ".join(words)
        return [word for word in words if combine.count(word) > 1]
