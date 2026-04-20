from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    """
    Solution using binary search

    Time complexity: O(n + m log n) where n is the length of nums and m is the length of queries
    Space complexity: O(n) for the memo dictionary
    """

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        memo = defaultdict(list)

        for i, num in enumerate(nums):
            memo[num].append(i)

        ans = []
        for q in queries:
            indices = memo[nums[q]]

            if len(indices) == 1:
                ans.append(-1)
            else:
                i = bisect_left(indices, q)

                j1 = indices[i - 1]
                j2 = indices[(i + 1) % len(indices)]

                d1 = abs(q - j1)
                d2 = abs(q - j2)

                ans.append(min(d1, d2, n - d1, n - d2))

        return ans


class Solution2:
    """
    Solution using two passes to find the minimum distance for each index

    Time complexity: O(n + m) where n is the length of nums and m is the length of queries
    Space complexity: O(n) for the min_dist array and the memo dictionary
    """

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        min_dist = [float("inf")] * n

        memo = {}
        for i in range(2 * n):
            j = i % n
            if nums[j] in memo:
                min_dist[j] = min(min_dist[j], i - memo[nums[j]])
            memo[nums[j]] = i

        memo = {}
        for i in range(n - 1, -n, -1):
            if nums[i] in memo:
                min_dist[i] = min(min_dist[i], memo[nums[i]] - i)
            memo[nums[i]] = i

        return [-1 if min_dist[q] >= n else min_dist[q] for q in queries]
