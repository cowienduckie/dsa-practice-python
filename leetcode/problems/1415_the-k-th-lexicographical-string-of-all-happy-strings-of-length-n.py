from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ["a", "b", "c"]
        ans = ""

        def traverse(i: int, s: List[str]) -> bool:
            # If a happy string constructed, update k, then update answer if k reach 0
            if i == n:
                nonlocal k, ans
                k = k - 1
                if not k:
                    ans = "".join(s)
                    return True
                return False
            # Try to add characters into string by backtracking
            for c in chars:
                if i != 0 and s[i - 1] == c:
                    continue
                s.append(c)
                if traverse(i + 1, s):
                    return True
                s.pop()
            return False

        # Traverse and construct all permutations until k decrease to 0
        traverse(0, [])
        return ans
