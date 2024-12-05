from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Pre-compute the following values for each node:
        # 1. The height of the subtree rooted at that node (h)
        # 2. The depth of the node from the root (d)
        # 3. The max and second max height of each depth in the original tree, as A and B
        #
        # So, each query Q to remove node X, we can get the answer by:
        # 1. If X is the max height of its depth, answer = height[B] + depth[B], if B exists, else depth[B] - 1
        # 2. If X is NOT the max height of its depth, answer = height[A] + depth[A]
        height = dict({0: -1})
        depth = dict()
        max_height = dict()

        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            # Update the height of the current node, and recurse to its children
            height[node.val] = max(get_height(node.left), get_height(node.right)) + 1
            return height[node.val]

        def get_depth(node: Optional[TreeNode], dep: int) -> None:
            if not node:
                return
            # Update the two max heights of the current depth
            if dep not in max_height:
                max_height[dep] = (node.val, 0)
            else:
                if height[node.val] > height[max_height[dep][0]]:
                    max_height[dep] = (node.val, max_height[dep][0])
                elif height[node.val] > height[max_height[dep][1]]:
                    max_height[dep] = (max_height[dep][0], node.val)
            # Update the depth of the current node, and recurse to its children
            depth[node.val] = dep
            get_depth(node.left, dep + 1)
            get_depth(node.right, dep + 1)

        get_height(root)
        get_depth(root, 0)

        ans = []
        for q in queries:
            best, second = max_height[depth[q]]
            if q == best:
                ans.append(
                    height[second] + depth[second] if second else depth[best] - 1
                )
            else:
                ans.append(height[best] + depth[best])

        return ans
