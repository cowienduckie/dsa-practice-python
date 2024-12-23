from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = 0
        while queue:
            # Traverse the current level
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                # Add children into BFS queue if they are not null
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Count swaps of the current level
            ans += self.count_min_swaps(level_values)

        return ans

    def count_min_swaps(self, source: List[int]) -> int:
        swaps = 0
        target = sorted(source)

        # Store the current position of each value in source list
        pos = {val: i for i, val in enumerate(source)}

        for i in range(len(source)):
            # If the i-th value has wrong position, find the right one then swap them
            if source[i] != target[i]:
                swaps += 1
                j = pos[target[i]]
                # Swap the i and j values and positions
                source[i], source[j] = source[j], source[i]
                pos[source[i]] = i
                pos[source[j]] = j

        return swaps
