from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], prev: int) -> int:
            if not node:
                return 0

            curr = prev * 2 + (1 if node.val == 1 else 0)

            if not node.left and not node.right:
                return curr

            return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)
