from typing import List


class Solution:
    """
    To find the maximum rotation function, we can derive a relationship
    between the initial rotation F(0) and the k-th rotation F(k).

    Let the total sum of the array be `sum(A) = A[0] + A[1] + ... + A[n-1]`.
    Let the sum of the last `k` elements be `suffix_k = A[n-k] + ... + A[n-1]`.
    Let the sum of the remaining elements be `prefix_k = sum(A) - suffix_k`.

    The typical transition from F(k-1) to F(k) is:
    F(k) = F(k-1) + sum(A) - n * A[n-k]

    If we expand this to calculate F(k) directly from F(0), we get:
    F(k) = F(0) + k * sum(A) - n * (A[n-1] + A[n-2] + ... + A[n-k])
    F(k) = F(0) + k * (prefix_k + suffix_k) - n * suffix_k
    F(k) = F(0) + k * prefix_k - (n - k) * suffix_k

    By iteratively maintaining the `prefix` and `suffix` sums, we can compute
    each F(k) in O(1) time and find the maximum over all k in O(N) total time.
    """

    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculate the initial rotation value F(0)
        ans = s = sum([i * nums[i] for i in range(n)])

        # Initially (k=0), the prefix sum is the whole array sum
        # and the suffix sum is 0.
        prefix = sum(nums)
        suffix = 0

        # Calculate F(k) for rotations k from 1 to n-1
        for k in range(1, n):
            # For rotation k, the element A[n-k] shifts from the end of
            # the prefix to the beginning of the suffix.
            prefix -= nums[n - k]
            suffix += nums[n - k]

            # Apply the derived formula to calculate F(k) and track the maximum
            ans = max(ans, s - (n - k) * suffix + k * prefix)

        return ans
