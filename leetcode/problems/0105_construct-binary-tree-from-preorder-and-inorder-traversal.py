from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    In preorder traversal, the first element is the root of the tree.
    In inorder traversal, the root element divides the inorder list into left and right subtrees respectively.

    So, we can use divide and conquer to build the tree recursively by finding the root element in each list.
    And construct the left and right subtrees recursively.
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_pos = inorder.index(preorder[0])

        return TreeNode(
            val=preorder[0],
            left=self.buildTree(preorder[1 : root_pos + 1], inorder[:root_pos]),
            right=self.buildTree(preorder[root_pos + 1 :], inorder[root_pos + 1 :]),
        )


class Solution2:
    """
    Optimized version of Solution 1 using a hashmap to store the index of each element in the inorder list.
    So that we can avoid the index() function which has a time complexity of O(n).
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: pos for pos, val in enumerate(inorder)}

        def dfs(start_pos: int, end_pos: int) -> Optional[TreeNode]:
            if start_pos > end_pos:
                return None

            root_val = preorder.pop(0)
            root_pos = inorder_map[root_val]
            return TreeNode(
                val=root_val,
                left=dfs(start_pos, root_pos - 1),
                right=dfs(root_pos + 1, end_pos),
            )

        return dfs(0, len(preorder) - 1)
