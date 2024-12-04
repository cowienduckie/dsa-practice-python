from typing import Dict, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.copied_dict: Dict[Node, Node] = {}

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        if node in self.copied_dict:
            return self.copied_dict[node]

        self.copied_dict[node] = Node(node.val)

        for next_node in node.neighbors:
            self.copied_dict[node].neighbors.append(self.cloneGraph(next_node))

        return self.copied_dict[node]
