from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Solution using Graph conversion and the Djikstra's algorithm to find the shortest path
    """

    def ladderLength(self, start_word: str, end_word: str, words: List[str]) -> int:
        # Find the indices of starting and ending words
        start = end = -1
        for i, word in enumerate(words):
            if word == start_word:
                start = i
            if word == end_word:
                end = i
        if end == -1:
            return 0
        if start == -1:
            start = len(words)
            words.append(start_word)

        # Add the adjacencies into the graph
        n = len(words)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if self.is_valid(words[i], words[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # Find shortest path from start to end using Djikstra's algorithm
        dist = [float("inf")] * n
        dist[start] = 0
        visited = [False] * n

        pq = [(0, start)]
        while pq:
            curr_dist, node = heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            for next_node in graph[node]:
                if curr_dist + 1 < dist[next_node]:
                    dist[next_node] = curr_dist + 1
                    heappush(pq, (dist[next_node], next_node))

        # Return the shortest path, if it exists
        return dist[end] + 1 if dist[end] != float("inf") else 0
