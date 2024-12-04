from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(start: int, curr_sum: int, combination: List[int]) -> None:
            if curr_sum == target:
                ans.append(combination)
                return

            for i in range(start, len(candidates)):
                if curr_sum + candidates[i] > target:
                    continue
                dfs(i, curr_sum + candidates[i], combination + [candidates[i]])

        dfs(0, 0, [])
        return ans
