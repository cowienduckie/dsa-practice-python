import string


class UnionFind:
    def __init__(self):
        self.parent = {char: char for char in string.ascii_lowercase}

    def find(self, char: str) -> str:
        if self.parent[char] != char:
            self.parent[char] = self.find(self.parent[char])

        return self.parent[char]

    def union(self, char1: str, char2: str) -> None:
        root1 = self.find(char1)
        root2 = self.find(char2)

        self.parent[root1] = root2

    def is_connected(self, char1: str, char2: str) -> bool:
        return self.find(char1) == self.find(char2)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for c1, c2 in zip(s1, s2):
            uf.union(c1, c2)

        ans = []
        for c1 in baseStr:
            for c2 in string.ascii_lowercase:
                if uf.is_connected(c1, c2):
                    ans.append(c2)
                    break

        return "".join(ans)
