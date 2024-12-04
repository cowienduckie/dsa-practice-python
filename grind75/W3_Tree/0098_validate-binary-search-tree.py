from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            if not node:
                return True
            elif not min_val < node.val < max_val:
                return False
            return traverse(node.left, min_val, node.val) and traverse(
                node.right, node.val, max_val
            )

        return traverse(root, float("-inf"), float("inf"))
