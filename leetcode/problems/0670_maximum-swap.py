class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num

        s = str(num)[::-1]
        diff = float("-inf")
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                diff = max(diff, (int(s[j]) - int(s[i])) * (10**i - 10**j))

        return num + diff if diff > 0 else num
