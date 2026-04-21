from collections import defaultdict
from typing import Counter, List


class UnionFind:
    def __init__(self, n: int):
        self.root = list(range(n))

    def _find(self, node: int) -> int:
        if node != self.root[node]:
            return self._find(self.root[node])
        return node

    def union(self, node1: int, node2: int) -> None:
        root1 = self._find(node1)
        root2 = self._find(node2)
        self.root[root1] = root2

    def get_groups(self) -> List[int]:
        """Return index groups for each connected component."""
        groups = defaultdict(list)
        for i in range(len(self.root)):
            groups[self._find(i)].append(i)
        return groups.values()


class Solution:
    """
    Solution using Union-Find to group indices that can be swapped,
    then comparing the frequency of values in each group to compute the minimum Hamming distance.

    Time Complexity: O(n + m * α(n))
        where n is the length of source/target and m is the number of allowed swaps,
        and α is the inverse Ackermann function.
    Space Complexity: O(n)
    """

    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        # Build the Union-Find structure based on allowed swaps
        n = len(source)
        uf = UnionFind(n)
        for i, j in allowedSwaps:
            uf.union(i, j)

        # Loop though each group of indices and count the frequency of values in source and target
        groups = uf.get_groups()
        diff = 0
        for group in groups:
            src = Counter([source[i] for i in group])
            tgt = Counter([target[i] for i in group])
            cmp = defaultdict(int)
            for k, v in src.items():
                cmp[k] += v
            for k, v in tgt.items():
                cmp[k] -= v
            for v in cmp.values():
                diff += abs(v)
        return diff // 2


print(
    Solution().minimumHammingDistance(
        source=[1, 2, 3, 4], target=[1, 3, 2, 4], allowedSwaps=[]
    )
)
