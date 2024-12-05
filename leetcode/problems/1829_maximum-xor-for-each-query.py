from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xor = [nums[0]] * n
        for i in range(1, n):
            xor[i] = xor[i - 1] ^ nums[i]

        max_ans = (1 << maximumBit) - 1
        for i in range(n):
            xor[i] = (xor[i] - ((xor[i] >> maximumBit) << maximumBit)) ^ max_ans

        xor.reverse()
        return xor


class Solution:
    """
    Optimized solution using only one loop.
    """

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = [(1 << maximumBit) - 1]
        for num in nums:
            ans.append(ans[-1] ^ num)

        return ans[len(nums) : 0 : -1]
