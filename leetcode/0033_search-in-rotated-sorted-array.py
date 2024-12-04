from typing import List


class Solution:
    """
    The search is performed in O(log n) time complexity.
    """

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        def binary_search(low: int, high: int) -> int:
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return -1

        if nums[0] > nums[-1]:
            # The array is rotated -> Binary search on the potential part
            def find_pivot_index() -> int:
                low = 0
                high = n - 1
                while low < high - 1:
                    mid = low + (high - low) // 2
                    if nums[mid] < nums[high]:
                        high = mid
                    else:
                        low = mid
                return low

            pivot = find_pivot_index()

            if target >= nums[0]:
                return binary_search(0, pivot + 1)
            else:
                return binary_search(pivot + 1, n)
        else:
            # The array is not rotated -> Binary search on the whole array
            return binary_search(0, n)
