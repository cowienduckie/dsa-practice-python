class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff % 2 == low % 2 == 0:
            return diff // 2
        else:
            return diff // 2 + 1
