from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Solution using heap or priority queue

    Assume that the first and last marble is fixed
    And, when we pick marble[i] as end of a bag, the marble[i + 1] is the start of next bag

    So, in case we need a maximum cost, we have to find k - 1 greatest pairs (marble[i], marble[i + 1])
    The same idea for a minimum cost.
    """

    def putMarbles(self, weights: List[int], k: int) -> int:
        # Base case
        n = len(weights)
        if n < 3:
            return 0

        # Total cost is always including the first and last marble
        min_cost = max_cost = weights[0] + weights[-1]

        # Use a min heap to find k - 1 smallest pairs
        min_heap = []
        for i in range(n - 1):
            heappush(min_heap, weights[i] + weights[i + 1])

        for _ in range(k - 1):
            min_cost += heappop(min_heap)

        # Use a max heap to find k - 1 greatest pairs
        max_heap = []
        for i in range(n - 1):
            heappush(max_heap, (weights[i] + weights[i + 1]) * -1)

        for _ in range(k - 1):
            max_cost += heappop(max_heap) * -1

        # Return the diff between max and min total cost
        return max_cost - min_cost


class Solution:
    """
    Solution using sorting for optimization
    """

    def putMarbles(self, weights: List[int], k: int) -> int:
        # Base case
        n = len(weights)
        if n < 3:
            return 0

        # Sort all pairs by their weight
        pairs = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pairs.sort()

        # Compute difference between the k - 1 smallest and greatest pairs
        diff = 0
        for i in range(k - 1):
            diff -= pairs[i]
            diff += pairs[-1 - i]

        return diff
