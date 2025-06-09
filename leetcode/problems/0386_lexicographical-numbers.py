from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(num: int) -> None:
            # Base case
            if num > n:
                return
            # Append current number to answer and try to adding 1 more digit after it
            ans.append(num)
            for i in range(10):
                dfs(num * 10 + i)

        # Pick the first digit from 1 to 9
        for i in range(1, 10):
            dfs(i)
        return ans
