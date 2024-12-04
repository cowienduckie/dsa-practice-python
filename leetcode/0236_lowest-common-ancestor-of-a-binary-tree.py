class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # If the root is one of the nodes, return the root
        if root == p or root == q:
            return root

        # Try to find the nodes in the left and right subtrees
        left, right = None, None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # If both nodes are found in the left and right subtrees, return the root
        if left and right:
            return root

        return left or right
