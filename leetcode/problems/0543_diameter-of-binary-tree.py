from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            # Base case
            if not node:
                return 0
            # Traverse both left and right sub-tree to get depth
            left = dfs(node.left)
            right = dfs(node.right)
            # Update answer
            nonlocal ans
            ans = max(ans, left + right)
            return max(left + 1, right + 1)

        dfs(root)
        return ans
