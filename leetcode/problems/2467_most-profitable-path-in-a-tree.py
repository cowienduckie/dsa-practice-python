from collections import defaultdict, deque
from typing import List


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        n = len(amount)

        # Add neighbor nodes for each node
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Find parent for each node recursively
        parent = [-1] * n

        def traverse(node: int) -> None:
            for neighbor in tree[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                traverse(neighbor)

        traverse(0)

        # Use BFS to test on cases
        ans = float("-inf")
        queue = deque([(0, bob, set(), 0)])  # A position, B position, B visited, income

        while queue:
            # Extract the tuple data
            pos_a, pos_b, visited, income = queue.popleft()

            # If A and B are in a same gate, share the cost/reward
            if pos_a == pos_b:
                income += amount[pos_a] // 2
            # If A is in a visited gate by B, do not take the cost/reward
            elif pos_a not in visited:
                income += amount[pos_a]

            # If A reach a leaf, update the answer
            if len(tree[pos_a]) == 1 and pos_a != 0:
                ans = max(ans, income)

            # Mark the position of B is visited until reach the root
            if pos_b != 0:
                visited.add(pos_b)

            # Because A have multiple choices to go but B have only one way to current node's parent
            # Try every neighbors of A's current node, except its parent
            for neighbor in tree[pos_a]:
                if neighbor == parent[pos_a]:
                    continue
                queue.append(
                    (neighbor, parent[pos_b] if pos_b != 0 else 0, visited, income)
                )

        return ans
