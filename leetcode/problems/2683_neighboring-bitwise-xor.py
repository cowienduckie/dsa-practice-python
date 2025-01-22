class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for bit in derived:
            ans ^= bit
        return ans == 0
