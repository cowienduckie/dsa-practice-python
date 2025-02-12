from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Solution using dictionary and max heap
    """

    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        # For each number, put it into dictionary by its digit sum
        memo = defaultdict(list)
        for num in nums:
            ds = self.digit_sum(num)
            heappush(memo[ds], -1 * num)
        # For each digit sum, try update the answer with sum of the two greatest
        ans = -1
        for heap in memo.values():
            if len(heap) >= 2:
                ans = max(ans, -(heappop(heap) + heappop(heap)))
        return ans

    def digit_sum(self, num: int) -> int:
        return sum(int(d) for d in str(num))


class Solution:
    """
    Solution using dictionary and 2-element array to store the two greatest numbers
    """

    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        # For each number, put it into dictionary by its digit sum
        memo = defaultdict(list)
        for num in nums:
            ds = self.digit_sum(num)
            if len(memo[ds]) < 2:
                memo[ds].append(num)
            else:
                memo[ds].sort()
                if num > memo[ds][0]:
                    memo[ds][0] = num
        # For each digit sum, try update the answer with sum of the two greatest
        ans = -1
        for arr in memo.values():
            if len(arr) == 2:
                ans = max(ans, arr[0] + arr[1])
        return ans

    def digit_sum(self, num: int) -> int:
        return sum(int(d) for d in str(num))


# For further optimization
#   1. Should break cases to maintain the 2 greatest instead of using built-in sort
#   2. Should implement the digit sum calculation using math way (looping divide and modulo by 10)
