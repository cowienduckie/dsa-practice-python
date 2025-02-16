from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [None] * ((n - 1) * 2 + 1)
        taken = [None] * (n + 1)
        if self.can_construct(0, ans, n, taken):
            return ans
        return []

    def can_construct(self, i: int, ans: int, n: int, taken: List[int]) -> bool:
        # If the current index is the last index, return True
        if i == len(ans):
            return True
        # If the current index is already filled, move to the next index
        if ans[i]:
            return self.can_construct(i + 1, ans, n, taken)
        # Try to fill the current index with the largest number as possible
        for x in range(n, 1, -1):
            if not taken[x] and i + x < len(ans) and not ans[i + x]:
                taken[x] = ans[i] = ans[i + x] = x
                if self.can_construct(i + 1, ans, n, taken):
                    return True
                taken[x] = ans[i] = ans[i + x] = None
        # If the largest number is not possible, try to fill the current index with 1
        if not taken[1]:
            taken[1] = ans[i] = 1
            if self.can_construct(i + 1, ans, n, taken):
                return True
            taken[1] = ans[i] = None
        return False


print(Solution().constructDistancedSequence(3))  # [3, 1, 2, 3, 2]
