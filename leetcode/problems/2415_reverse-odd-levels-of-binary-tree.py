from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, 0)])
        odd = deque()
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
            if level & 1:
                odd.append(node)
            else:
                while len(odd) > 1:
                    front = odd.popleft()
                    back = odd.pop()
                    front.val, back.val = back.val, front.val
                odd.clear()

        while len(odd) > 1:
            front = odd.popleft()
            back = odd.pop()
            front.val, back.val = back.val, front.val

        return root
