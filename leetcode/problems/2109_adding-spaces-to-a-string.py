from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index, ans = 0, []
        spaces.append(len(s))

        for space in spaces:
            ans.append(s[index:space])
            index = space

        return " ".join(ans)
