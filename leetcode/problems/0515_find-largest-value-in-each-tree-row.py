from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # If tree has no node, return empty
        if not root:
            return []

        # Use BFS to traverse through each level
        queue = deque([root])
        ans = []
        while queue:
            level_size = len(queue)
            level_values = []
            # Extract all node's values of each level
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                # Add the children to queue if they're not null
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Add the max value of each level
            ans.append(max(level_values))

        return ans
