class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        visited = False
        for c in s:
            if c == '0':
                visited = True
            elif visited:
                return False
        return True