from collections import defaultdict
from typing import List


class Component:
    def __init__(self):
        self.nodes = 0
        self.edges = 0


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Use dictionary to store the graph as adjacencies list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use DFS to find the component each node belonging
        marked = [0] * n

        def dfs(u: int, component: int) -> None:
            # Return if node u have already belongs to some component
            if marked[u] != 0:
                return
            # Mark node u in component
            marked[u] = component
            # Traverse to the neighbors of node u
            for v in graph[u]:
                dfs(v, component)

        # Iterate through all nodes and try to start a new component if node u is unmarked
        component_cnt = 0
        for u in range(n):
            if marked[u] != 0:
                continue
            component_cnt += 1
            dfs(u, component_cnt)

        # Count number of nodes and edges in each component
        components = {i: Component() for i in range(1, component_cnt + 1)}

        for i in marked:
            components[i].nodes += 1

        for u, _ in edges:
            components[marked[u]].edges += 1

        # Check if any component is completed
        ans = 0
        for comp in components.values():
            if comp.edges == (comp.nodes - 1) * comp.nodes // 2:
                ans += 1

        return ans
