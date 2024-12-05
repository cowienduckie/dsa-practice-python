class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for pos in range(n):
            if s[:pos] == goal[n - pos :] and s[pos:] == goal[: n - pos]:
                return True
        return False
