from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Solution using Dijkstra algorithm
    """

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007

        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Initialize distances and counts
        min_times = [float("inf")] * n
        path_counts = [0] * n

        min_times[0] = 0
        path_counts[0] = 1

        # Use Dijkstra algorithm to find the shortest path and count
        heap = [(0, 0)]

        while heap:
            curr_time, u = heappop(heap)
            # Skip if current time is greater than the minimum time
            if curr_time > min_times[u]:
                continue
            # Traverse to the neighbors v of node u
            for v, time in graph[u]:
                new_time = curr_time + time
                # Update times and counts if new_time is smaller
                if new_time < min_times[v]:
                    min_times[v] = new_time
                    path_counts[v] = path_counts[u]
                    heappush(heap, (new_time, v))
                # Update counts if new_time is equal
                elif new_time == min_times[v]:
                    path_counts[v] = (path_counts[v] + path_counts[u]) % MOD

        return path_counts[n - 1]


class Solution:
    """
    Solution using Floyd-Warshall algorithm
    """

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007

        # Use two separate 2D arrays for time and count
        min_times = [[float("inf")] * n for _ in range(n)]
        path_counts = [[0] * n for _ in range(n)]

        # Initialize times and counts
        for u in range(n):
            min_times[u][u] = 0
            path_counts[u][u] = 1

        for u, v, time in roads:
            min_times[u][v] = time
            min_times[v][u] = time
            path_counts[u][v] = 1
            path_counts[v][u] = 1

        # Floyd-Warshall algorithm
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    # Skip if no path through k
                    if (
                        min_times[u][k] == float("inf")
                        or min_times[k][v] == float("inf")
                        or k == u
                        or k == v
                    ):
                        continue

                    new_time = min_times[u][k] + min_times[k][v]

                    # Update times and counts if new_time is smaller
                    if new_time < min_times[u][v]:
                        min_times[u][v] = new_time
                        path_counts[u][v] = (
                            path_counts[u][k] * path_counts[k][v]
                        ) % MOD
                    # Update counts if new_time is equal
                    elif new_time == min_times[u][v]:
                        path_counts[u][v] = (
                            path_counts[u][v] + (path_counts[u][k] * path_counts[k][v])
                        ) % MOD

        return path_counts[0][n - 1]
