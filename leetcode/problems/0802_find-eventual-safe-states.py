from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [True] * n  # Mark node i as safe or not
        checked = [False] * n  # Mark node i as checked its neighbors or not
        visited = [False] * n  # Track the visited for current traversing stack

        # Use dfs with backtracking to detect the loops
        # Every nodes with same traversing stack of a loop is unsafe
        def dfs(node: int) -> bool:
            # Loop found
            if visited[node]:
                return True
            # All outgoing path is considered
            if checked[node]:
                return False

            checked[node] = True
            visited[node] = True
            for neighbor in graph[node]:
                # If a loop found, return immediately to spread the unsafe marks
                if dfs(neighbor):
                    safe[node] = False
                    return True

            visited[node] = False
            return False

        # Run DFS for each starting node
        for node in range(n):
            dfs(node)
        # Filter to take the safe ones only
        return [node for node in range(n) if safe[node]]
