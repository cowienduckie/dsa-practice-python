from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a dictionary to store all nodes in graph, ignoring the duplicates
        graph = {}

        for num in nums:
            if num in graph:
                continue
            # If node with value num is not in graph, create new one
            graph[num] = Node(num)

            # Try add the previous node if existed
            if num - 1 in graph:
                graph[num].prev = graph[num - 1]
                graph[num - 1].next = graph[num]

            # Try add the next node if existed
            if num + 1 in graph:
                graph[num].next = graph[num + 1]
                graph[num + 1].prev = graph[num]

        # Try to traverse through all nodes and find the largest components
        visited = set()

        def traverse(node: Optional[Node]) -> int:
            # Base cases
            if not node or node.value in visited:
                return 0
            visited.add(node.value)

            # Traverse to next and prev nodes and return the size
            return traverse(node.next) + traverse(node.prev) + 1

        # Update answer with sizes of components
        ans = 0
        for node in graph.values():
            ans = max(ans, traverse(node))

        return ans
