from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Flip operation is not affected to parent-child relationship between nodes
        # So, we only need to compare all relationships in both tree
        parents = [None] * 100

        def dfs(node: Optional[TreeNode], parent_val: int) -> None:
            if not node:
                return

            parents[node.val] = None if parents[node.val] is not None else parent_val
            dfs(node.left, node.val)
            dfs(node.right, node.val)

        dfs(root1, -1)
        dfs(root2, -1)

        return not any(parent is not None for parent in parents)


class Test:
    def __init__(self, tree1: List[int], tree2: List[int]):

        self.root1 = self.make_tree(tree1)
        self.root2 = self.make_tree(tree2)

    def make_tree(self, nodes: List[int]):
        def dfs(index: int) -> Optional[TreeNode]:
            if index >= len(nodes) or nodes[index] is None:
                return None

            return TreeNode(nodes[index], dfs(2 * index + 1), dfs(2 * index + 2))

        return dfs(0) if nodes else None

    def run(self):
        print(Solution().flipEquiv(self.root1, self.root2))


Test([1, 2, 3], [1, 2, None, 3]).run()
