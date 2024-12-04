from typing import List


class BitCounter:
    def __init__(self):
        self.bits = [0] * 32

    def to_value(self) -> int:
        return sum(1 << i for i in range(32) if self.bits[i])

    def add(self, num: int) -> None:
        for i in range(32):
            if num & (1 << i):
                self.bits[i] += 1

    def remove(self, num: int) -> None:
        for i in range(32):
            if num & (1 << i):
                self.bits[i] -= 1

    def reset(self) -> None:
        self.bits = [0] * 32


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bit_counter = BitCounter()
        n = len(nums)
        l, curr_or = 0, 0
        ans = float("inf")

        for r in range(n):
            # If the current OR is less than or equal to the current number, we reset the counter.
            # Otherwise, we add the current number to the counter.
            if curr_or | nums[r] <= nums[r]:
                l = r
                curr_or = nums[r]
                bit_counter.reset()
                bit_counter.add(nums[r])
            else:
                curr_or |= nums[r]
                bit_counter.add(nums[r])

            # If we found a valid subarray, try to shrink it by removing leftmost elements.
            while l <= r < n and curr_or >= k:
                ans = min(ans, r - l + 1)
                # Try to remove the leftmost element from the counter.
                bit_counter.remove(nums[l])
                curr_or = bit_counter.to_value()
                l += 1

        return ans if ans != float("inf") else -1


print(Solution().minimumSubarrayLength([1, 2], 0))
