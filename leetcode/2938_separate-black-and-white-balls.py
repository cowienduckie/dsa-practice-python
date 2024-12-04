class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        white = 0
        for i in range(n):
            if s[i] == "0":
                white = white + 1

        pairs, steps = 0, 0
        for i in range(white):
            if s[i] == "1":
                pairs += 1
                steps += white - i - 1
        for i in range(white, n):
            if s[i] == "0":
                steps += i - white

        return steps + pairs
