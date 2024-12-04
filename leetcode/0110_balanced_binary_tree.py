from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) >= 0

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1
