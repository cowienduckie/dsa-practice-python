from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Track frequency of each digit
        freq = Counter(digits)

        # Use DFS and backtracking to compute all valid combinations from digits
        conf = {
            1: {"digits": range(1, 10), "multiplier": 100},
            2: {"digits": range(10), "multiplier": 10},
            3: {"digits": range(0, 10, 2), "multiplier": 1},
        }
        ans = []

        def dfs(pos: int, num: int) -> None:
            if pos < 4:
                for d in conf[pos]["digits"]:
                    if freq[d] != 0:
                        freq[d] -= 1
                        dfs(pos + 1, num + d * conf[pos]["multiplier"])
                        freq[d] += 1
            else:
                ans.append(num)

        # Start the DFS from 0 and first digit
        dfs(1, 0)
        return ans


print(Solution().findEvenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
