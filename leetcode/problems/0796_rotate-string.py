class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        s = s + s
        for i in range(n):
            if goal == s[i : i + n]:
                return True
        return False
