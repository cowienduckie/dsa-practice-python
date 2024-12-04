from typing import List


class Solution:
    def validArrangement(self, edges: List[List[int]]) -> List[List[int]]:
        # Convert input into a directed graph
        # Save the adjacencies, in-degree, and out-degree of each node
        graph = {}
        in_degree = {}
        out_degree = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
                in_degree[u] = out_degree[u] = 0
            if v not in graph:
                graph[v] = []
                in_degree[v] = out_degree[v] = 0

            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1

        # The problem ensures that we have at least Eulerian path
        # If we have an Eulerian cycle, just pick a random node as starter
        # Otherwise, find the start which has more out-degree than in-degree exactly 1
        start = edges[0][0]
        for u in graph:
            if out_degree[u] - in_degree[u] == 1:
                start = u
                break

        # Use DFS to traverse the graph
        path = []

        def dfs(u: int) -> None:
            # Use post-ordered DFS to add the edges into correct path
            while graph[u]:
                v = graph[u].pop()
                dfs(v)
                path.append([u, v])

        dfs(start)
        return path[::-1]
