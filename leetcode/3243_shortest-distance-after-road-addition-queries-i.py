from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        graph = {x: [x + 1] if x < n - 1 else [] for x in range(n)}
        dist = list(range(n))  # Distances from 0 to node i-th

        def update_dist(u: int, v: int) -> List[int]:
            # Add new edge into graph
            graph[u].append(v)

            # Use Dijkstra and BFS to maintain dist
            heap = [(dist[u], u)]
            visited = set()
            while heap:
                curr, node = heappop(heap)
                # Check if node has been visited yet
                if node in visited:
                    continue
                visited.add(node)

                # Update adjacencies if possible
                for next in graph[node]:
                    if curr + 1 < dist[next]:
                        dist[next] = curr + 1
                        heappush(heap, (dist[next], next))
            return dist

        return [update_dist(u, v)[n - 1] for u, v in queries]
