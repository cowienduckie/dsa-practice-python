from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Calculate the prefix sum of each subarray of length k
        prefix = [0] * n
        prefix[k - 1] = sum(nums[0:k])
        for i in range(k, n):
            prefix[i] = prefix[i - 1] + nums[i] - nums[i - k]

        def calculate_sum(end_indices: List[int]) -> int:
            return sum(prefix[i] for i in end_indices)

        # Store the index of the maximum subarray ending at i
        best_single = [None] * n
        best_single[k - 1] = [k - 1]
        for i in range(k, n):
            if prefix[i] > calculate_sum(best_single[i - 1]):
                best_single[i] = [i]
            else:
                best_single[i] = best_single[i - 1]

        # Store the indices of the maximum sum of two sub-arrays ending at i
        best_double = [None] * n
        best_double[2 * k - 1] = [k - 1, 2 * k - 1]
        for i in range(2 * k, n):
            if calculate_sum(best_single[i - k] + [i]) > calculate_sum(
                best_double[i - 1]
            ):
                best_double[i] = best_single[i - k] + [i]
            else:
                best_double[i] = best_double[i - 1]

        # Store the indices of the maximum sum of three sub-arrays ending at i
        best_triplet = [None] * n
        best_triplet[3 * k - 1] = [k - 1, 2 * k - 1, 3 * k - 1]
        for i in range(3 * k, n):
            if calculate_sum(best_double[i - k] + [i]) > calculate_sum(
                best_triplet[i - 1]
            ):
                best_triplet[i] = best_double[i - k] + [i]
            else:
                best_triplet[i] = best_triplet[i - 1]

        # Return the starting indices of the best triplet
        return [i - k + 1 for i in best_triplet[n - 1]]
