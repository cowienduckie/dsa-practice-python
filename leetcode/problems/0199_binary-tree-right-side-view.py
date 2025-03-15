from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Base cases
        if not root:
            return []

        # Use BFS to find the rightmost node at each level
        queue = deque([root])
        ans = []

        while queue:
            # Add the rightmost node's value into answer
            ans.append(queue[-1].val)

            # Pop all current level's nodes and add their children
            for _ in range(len(queue)):
                node = queue.popleft()
                # Append children if they are not null
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans
