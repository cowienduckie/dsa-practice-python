from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def traverse(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0

            smaller = traverse(node.left, target) + 1
            if smaller == target:
                nonlocal ans
                ans = node.val
                return float("inf")

            return smaller + (
                traverse(node.right, target - smaller) if smaller < target else 0
            )

        traverse(root, k)

        return ans
