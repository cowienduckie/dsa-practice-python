from typing import List


class Solution:
    """
    Solution with O(n) extra space complexity
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Compute prefix product of each index i (not including i)
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        # Compute suffix product of each index i (not including i)
        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        # Combine answer
        return [prefix[i] * suffix[i] for i in range(n)]


class Solution2:
    """
    Optimized solution with O(1) extra space complexity (excluding the output array)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_prod = [1] * n
        # Calculate the product of all elements to the left of the current element
        tmp_prod = 1
        for i in range(1, n):
            tmp_prod = tmp_prod * nums[i - 1]
            ans_prod[i] *= tmp_prod
        # Calculate the product of all elements to the right of the current element
        tmp_prod = 1
        for i in range(n - 2, -1, -1):
            tmp_prod = tmp_prod * nums[i + 1]
            ans_prod[i] *= tmp_prod
        return ans_prod
