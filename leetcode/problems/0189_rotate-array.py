from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Ignore the unaffected n-step rotate
        k = k % n

        # Clone the array
        clone = [num for num in nums]

        # Update the original array in-place
        for i in range(n):
            nums[i] = clone[i - k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Ignore the unaffected n-step rotate
        k = k % n

        # Update the array recursively with O(1) extra space
        updated = 0

        def update(i: int, value: int, end: int) -> None:
            if i != end:
                update((i + k) % n, nums[i], end)
            nums[i] = value
            nonlocal updated
            updated += 1

        start = 0
        while updated < n:
            update((start + k) % n, nums[start], start)
            start += 1
