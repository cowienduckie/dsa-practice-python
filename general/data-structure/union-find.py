class UnionFind:
    """
    Union Find is a data structure that keeps track of elements which are split into one or more disjoint sets.
    Complexity:
        - Find: O(log n)
        - Basic Union: O(log n)
        - Rank Union (Optimized version of Basic Union): O(log n)
        - Connected: O(log n)
        - Space: O(n)
    """

    def __init__(self, number_of_nodes: int):
        """
        Initialize the Union Find data structure with 2 lists:
            - parent: list of the parent of each node
            - rank: list of the rank of each node
        """
        self.parent = list(range(number_of_nodes))
        self.rank = [0] * number_of_nodes

    def find(self, node: int) -> int:
        """
        Find the root of the node
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def basic_union(self, node1: int, node2: int) -> None:
        """
        Connect two nodes by setting one of two roots as the parent of the other
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        self.parent[root1] = root2

    def rank_union(self, node1: int, node2: int) -> None:
        """
        Connect two nodes by setting one of two roots as the parent of the other.
        The rank of the root is used to determine which root should be the parent.
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

    def connected(self, node1: int, node2: int) -> bool:
        """
        Check if two nodes are connected
        """
        return self.find(node1) == self.find(node2)
