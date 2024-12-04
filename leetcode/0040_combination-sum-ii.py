from typing import List


class Solution:
    ans = []
    arr = []
    combination = []
    target = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.arr = sorted(candidates)
        self.combination = []
        self.target = target

        self.calculate_sum(0, 0)

        return self.ans

    def calculate_sum(self, start: int, curr_sum: int) -> None:
        if curr_sum == self.target:
            self.ans.append(self.combination.copy())
            return
        elif curr_sum > self.target:
            return

        for pos in range(start, len(self.arr)):
            if pos > start and self.arr[pos] == self.arr[pos - 1]:
                continue

            self.combination.append(self.arr[pos])
            self.calculate_sum(pos + 1, curr_sum + self.arr[pos])
            self.combination.pop()
