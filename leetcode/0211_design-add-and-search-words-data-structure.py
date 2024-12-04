class WordDictionary:

    def __init__(self):
        self.root = dict()
        self.any_char = "."
        self.end_char = "#"

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, dict())
        node[self.end_char] = None

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return self.end_char in node

            if word[i] == self.any_char:
                return any(
                    dfs(i + 1, node[child]) for child in node if child != self.end_char
                )
            elif word[i] in node:
                return dfs(i + 1, node[word[i]])

            return False

        return dfs(0, self.root)
