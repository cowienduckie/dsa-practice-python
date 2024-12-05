from typing import Dict, List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Treat each stone as a node in graph
        # There is an edge between A and B if they share same row or col
        # Because each node can delete its adjacencies -> Able to delete the whole connected component until there is only 1 node left
        # -> The maximum number of nodes that can be deleted = total number of nodes - number of connected components

        n = len(stones)

        # Use adjacencies list to store the graph
        adj: Dict[int, List[int]] = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)

        # Mark visited nodes
        visited: List[bool] = [False for i in range(n)]
        count = 0  # Number of connected components

        # DFS to traverse
        def traverse(curr_node: int) -> None:
            if visited[curr_node]:
                return
            visited[curr_node] = True

            for next_node in adj[curr_node]:
                traverse(next_node)

        for i in range(n):
            if visited[i]:
                continue
            traverse(i)
            count = count + 1

        return n - count


print(Solution().removeStones([[3, 2], [3, 1], [4, 4], [1, 1], [0, 2], [4, 0]]))  # 4
