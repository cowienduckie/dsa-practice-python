from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Track the count of zeroes and the sum of each array
        zeroes_1 = zeroes_2 = sum_1 = sum_2 = 0
        for num in nums1:
            sum_1 += num
            if num == 0:
                sum_1 += 1
                zeroes_1 += 1
        for num in nums2:
            sum_2 += num
            if num == 0:
                sum_2 += 1
                zeroes_2 += 1

        # If both arrays not have any zero, return one's sum if they are equal, otherwise return -1
        if zeroes_1 == 0 and zeroes_2 == 0:
            return sum_1 if sum_1 == sum_2 else -1
        # If array A has zeroes but B doesn't, return sum of A if it is greater than or equal to B, otherwise return -1
        elif zeroes_1 == 0:
            return sum_1 if sum_1 >= sum_2 else -1
        elif zeroes_2 == 0:
            return sum_2 if sum_2 >= sum_1 else -1
        # If both arrays have zeroes, return the maximum sum
        else:
            return max(sum_1, sum_2)
