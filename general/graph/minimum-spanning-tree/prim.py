import heapq
from typing import List


class Solution:
    def prim_mst(n: int, edges: List[List[int]]) -> int:
        # Initialize graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Prim's algorithm
        ans = curr = 0
        dist = [float("inf")] * n
        visited = [False] * n
        for _ in range(n):
            visited[curr] = True
            # Update distance to neighbors that are not visited
            for v, w in graph[curr]:
                if not visited[v]:
                    dist[v] = min(dist[v], w)
            # Take one unvisited node with minimum distance to check next
            curr = min((i for i in range(n) if not visited[i]), key=lambda x: dist[x])
            # Add the shortest edge to the answer
            ans += dist[curr]
            # Reset distance to the current node
            dist[curr] = float("inf")

        return ans


class Solution2:
    def prim_mst(n: int, edges: List[List[int]]) -> int:
        # Initialize graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Prim's algorithm using a heap
        ans = 0
        visited = [False] * n
        min_heap = [(0, 0)]  # (weight, node)
        while min_heap:
            w, u = heapq.heappop(min_heap)
            # Skip visited nodes
            if visited[u]:
                continue
            visited[u] = True
            # Add the shortest edge to the answer
            ans += w
            # Add unvisited neighbors to the heap
            for v, w in graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
        return ans
