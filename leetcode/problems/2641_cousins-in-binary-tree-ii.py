from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use BFS to queue up all nodes with their level, and store each level sum
        queue = deque()
        queue.append((root, 0))
        level_sum = dict()

        while queue:
            node, level = queue.popleft()
            level_sum[level] = level_sum.get(level, 0) + node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Use BFS to update the children values
        queue.append((root, 0))
        root.val = 0
        while queue:
            node, level = queue.popleft()

            children_sum = 0
            children_sum += node.left.val if node.left else 0
            children_sum += node.right.val if node.right else 0

            if node.left:
                node.left.val = level_sum[level + 1] - children_sum
                queue.append((node.left, level + 1))

            if node.right:
                node.right.val = level_sum[level + 1] - children_sum
                queue.append((node.right, level + 1))

        return root
