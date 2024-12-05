from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p == q == None:
                return True
            elif p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        def traverse(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            return (
                traverse(node.right) or traverse(node.left) or isSameTree(node, subRoot)
            )

        return traverse(root)
