from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # Use sliding window to maintain the gas from index l to r
        # If the window size reach n, left pointer is the right answer
        l = r = curr_gas = 0
        while r < 2 * n:
            curr_gas += gas[r % n] - cost[r % n]
            r += 1
            if curr_gas < 0:
                curr_gas = 0
                l = r
                continue
            if r - l == n:
                return l
        return -1
