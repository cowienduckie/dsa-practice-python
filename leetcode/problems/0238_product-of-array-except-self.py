from typing import List


class Solution:
    """
    Solution with O(n) extra space complexity
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[n - 1 - i] = suffix[n - i] * nums[n - i]

        for i in range(n):
            prefix[i] *= suffix[i]

        return prefix


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
