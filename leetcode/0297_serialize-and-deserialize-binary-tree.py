from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.delimiter = ","
        self.none_node = "null"

    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        ans = ""

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

            ans += (
                self.delimiter + str(node.val)
                if node
                else self.delimiter + self.none_node
            )

        return ans[1:]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(self.delimiter)
        n = len(nodes)

        def dfs(pos: int) -> Optional[TreeNode]:
            if pos >= n or nodes[pos] == self.none_node:
                return None

            node = TreeNode(int(nodes[pos]))
            node.left = dfs(2 * pos + 1)
            node.right = dfs(2 * pos + 2)
            return node

        return dfs(0)


print(Codec().serialize(Codec().deserialize("1,2,3,null,null,4,5")))
