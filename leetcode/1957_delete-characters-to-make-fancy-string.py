class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        same_char = 0
        prev_char = ""

        for c in s:
            same_char = 1 + (same_char if c == prev_char else 0)
            if same_char < 3:
                ans.append(c)
            prev_char = c

        return "".join(ans)
