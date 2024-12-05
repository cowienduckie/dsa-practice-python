from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def make_combinations(num: int, combination: List[int], curr_len: int) -> None:
            # Base cases
            # - If the current combination has k elements, add it to the answer and return
            # - If the current number is greater than n, return
            if curr_len == k:
                ans.append(combination)
                return
            if num == n + 1:
                return

            # If there are enough numbers left to make a combination, the current number can be skipped
            if n - num + 1 > k - curr_len:
                make_combinations(num + 1, combination, curr_len)

            # Include the current number in the combination
            make_combinations(num + 1, combination + [num], curr_len + 1)

        make_combinations(1, [], 0)
        return ans
