from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution using Divide and Conquer
    Given a pre-order and post-order traversal of a binary tree, we can easily retrieve these information:
        - Root always the first element of pre-order and the last element of post-order
        - The second element of pre-order is the left child
        - The second last element of post-order is the right child
        - If left and right children are possibly the sam
    Approach:
        - Handle the base case from 0-2 nodes in tree
        - If more than 2 nodes, split the two traversals by subtrees and construct them recursively
    """

    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        # If there is no node, return None
        if not preorder and not postorder:
            return None

        # Create a node of first value in pre-order as root
        n = len(preorder)
        root = TreeNode(preorder[0])

        # If only root in the tree, return itself
        if n == 1:
            return root

        # If there are 2 nodes in tree, add the non-root node as child
        if n == 2:
            root.left = TreeNode(preorder[1])
            return root

        # If there are more than 2 nodes, we need to consider about left and right subtree
        left_val = preorder[1]
        right_val = postorder[n - 2]

        # Check if the left and right node is a same node
        if left_val == right_val:
            root.left = self.constructFromPrePost(preorder[1:], postorder[: n - 1])
        else:
            # Find index of right_val in pre-order
            i = 2
            while preorder[i] != right_val:
                i += 1

            # Find index of left_val in post-order
            j = n - 3
            while postorder[j] != left_val:
                j -= 1

            # Construct left and right subtree
            root.left = self.constructFromPrePost(preorder[1:i], postorder[: j + 1])
            root.right = self.constructFromPrePost(
                preorder[i:], postorder[j + 1 : n - 1]
            )

        return root
