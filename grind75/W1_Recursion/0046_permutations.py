from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Uses backtracking to generate all permutations of the given numbers.
        """
        n = len(nums)
        visited = [False] * n
        ans = []

        def make_permutations(arr: List[int], curr_len: int) -> None:
            # If the current permutation is complete, add it to the answer
            if curr_len == n:
                nonlocal ans
                ans.append(arr)
                return

            # For each number, add it to the current permutation if it hasn't been visited yet
            nonlocal visited
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                make_permutations(arr + [nums[i]], curr_len + 1)
                visited[i] = False

        make_permutations([], 0)
        return ans
