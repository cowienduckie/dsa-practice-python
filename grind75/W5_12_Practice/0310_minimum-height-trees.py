from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Base cases
        if n <= 2:
            return list(range(n))

        # Construct the graph with adjacencies list
        graph = {x: set() for x in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Create a leaves queue
        queue = deque([k for k, v in graph.items() if len(v) == 1])

        # While-loop and remove all leaves at each iteration
        while len(graph) > 2:
            leaves = len(queue)
            for _ in range(leaves):
                leaf = queue.popleft()
                parent = list(graph[leaf])[0]

                graph[parent].remove(leaf)
                graph.pop(leaf)

                if len(graph[parent]) == 1:
                    queue.append(parent)

        return list(queue)


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))  # [1]
