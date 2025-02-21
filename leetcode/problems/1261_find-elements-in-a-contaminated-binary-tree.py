from collections import set
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    """
    Simulation solution to recover the tree recursively and find nodes recursively
        - Recover O(n)
        - Find O(n)
    """

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.recover(root, 0)

    def find(self, target: int) -> bool:
        return self.find_node(self.root, target) is not None

    def find_node(self, node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # If node is null or its value greater than target, return None
        if not node or node.val > target:
            return None
        # If node's value is equal target return itself
        if node.val == target:
            return node
        # Find target in left or right subtree
        if (found_node := self.find_node(node.left, target)) is not None:
            return found_node
        else:
            return self.find_node(node.right, target)

    def recover(self, node: Optional[TreeNode], value: int) -> None:
        # If node is not null, update its value
        if not node:
            return
        node.val = value
        # Traverse 2 children
        self.recover(node.left, 2 * value + 1)
        self.recover(node.right, 2 * value + 2)


class FindElements:
    """
    Solution using set of existing value in the tree
        - Recover O(n)
        - Find O(1)
    """

    def __init__(self, root: Optional[TreeNode]):
        self.existing = set()
        self.recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.existing

    def recover(self, node: Optional[TreeNode], value: int) -> None:
        # If node is not null, add its value to the set
        if not node:
            return
        self.existing.add(value)
        # Traverse 2 children
        self.recover(node.left, 2 * value + 1)
        self.recover(node.right, 2 * value + 2)
