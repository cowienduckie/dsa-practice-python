from collections import deque
from heapq import heappop, heappush
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Use BFS to check every single level and push the sum of the level to a heap
        sum_heap = list()
        curr_level = 0
        queue = deque()
        queue.append((root, 0))

        while queue:
            level_sum = 0
            while queue and queue[0][1] == curr_level:
                node, lvl = queue.popleft()
                if node:
                    level_sum += node.val
                    queue.append((node.left, lvl + 1))
                    queue.append((node.right, lvl + 1))
            # Because all nodes are positive, there is no level with sum 0
            if level_sum:
                heappush(sum_heap, level_sum * -1)
            curr_level += 1

        # Pop k times from the heap to get the kth largest sum
        for _ in range(k - 1):
            if sum_heap:
                heappop(sum_heap)

        return heappop(sum_heap) * -1 if sum_heap else -1
