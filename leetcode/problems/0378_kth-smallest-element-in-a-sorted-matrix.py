from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    """
    Use a n-length array to store the min index of each row. At each iteration, find the min element then update the indices array.

    Time complexity: O(k * n)
    Space complexity: O(n)
    """

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, ans = len(matrix), 0
        indices = [0] * n

        for _ in range(k):
            curr_min = float("inf")
            min_row = 0

            for i in range(n):
                if indices[i] < n and matrix[i][indices[i]] < curr_min:
                    curr_min = matrix[i][indices[i]]
                    min_row = i

            indices[min_row] += 1
            ans = curr_min

        return ans


class Solution2:
    """
    Use a heap to store the min elements of each row. At each iteration, pop the min element then push the next element from the same row.

    Time complexity: O(k * log n)
    Space complexity: O(n)
    """

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]  # Store as (num, row, col)
        heapify(heap)

        for _ in range(k):
            num, row, col = heappop(heap)
            if col + 1 < n:
                heappush(heap, (matrix[row][col + 1], row, col + 1))

        return num


class Solution3:
    """
    Use binary search on the value range to find the kth smallest element.

    Time complexity: O(n * log(max-min))
    Space complexity: O(1)
    """

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_less_equal(x):
            count, n = 0, len(matrix)
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left
