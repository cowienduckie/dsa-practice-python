from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        def dfs(num: int, set_bits: int) -> None:
            if num > n:
                return
            ans[num] = set_bits

            dfs(num << 1, set_bits)
            dfs((num << 1) + 1, set_bits + 1)

        dfs(1, 1)
        return ans
