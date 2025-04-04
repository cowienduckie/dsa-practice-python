from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution using BFS twice by finding the deepest leaves first
    And then finding the common ancestor of them by traversing up through the parents
    """

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use BFS to traverse through tree by level and track node's parents
        # Additionally, find the deepest leaves
        queue = deque([(root, None)])
        parent = {}
        deepest = None

        while queue:
            level = []
            for _ in range(len(queue)):
                # Extract node and its parent
                node, parent_node = queue.popleft()
                # Update parent and level nodes
                parent[node] = parent_node
                level.append(node)
                # Add children to the queue, if any
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            # If the BFS finish, add the current level's nodes as deepest leaves
            if not queue:
                deepest = level

        # Use reversed BFS to find the common ancestor of all deepest leaves
        queue = deque(deepest)
        while len(queue) > 1:
            for _ in range(len(queue)):
                # Extract the node
                node = queue.popleft()
                # Add node's parent to queue if it is not added before
                if queue[-1].val != parent[node].val:
                    queue.append(parent[node])

        # Return the common ancestor of all deepest leaves
        return queue[0]


class Solution:
    """
    Solution using built-in set to ease the process of finding the common ancestor
    """

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use BFS to find the deepest leaves and their common ancestor
        # Initialize queue with root and its parent as None
        queue = deque([(root, None)])
        parent = {}
        deepest = None

        while queue:
            level = []
            for _ in range(len(queue)):
                # Extract node and its parent
                node, parent_node = queue.popleft()
                # Update parent and level nodes
                level.append(node)
                parent[node] = parent_node
                # Add children to the queue, if any
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            # If the BFS finish, add the current level's nodes as deepest leaves
            if not queue:
                deepest = set(level)

        # Use reversed BFS to find the common ancestor of all deepest leaves
        while len(deepest) > 1:
            deepest = set([parent[node] for node in deepest])

        # Return the common ancestor of all deepest leaves
        return list(deepest)[0]
