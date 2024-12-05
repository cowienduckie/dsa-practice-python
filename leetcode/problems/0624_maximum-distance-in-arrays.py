from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        best_max, second_max = (0, 1) if arrays[0][-1] > arrays[1][-1] else (1, 0)
        best_min, second_min = (0, 1) if arrays[0][0] < arrays[1][0] else (1, 0)

        for i in range(2, len(arrays)):
            if arrays[i][-1] >= arrays[best_max][-1]:
                second_max, best_max = best_max, i
            elif arrays[i][-1] > arrays[second_max][-1]:
                second_max = i

            if arrays[i][0] <= arrays[best_min][0]:
                second_min, best_min = best_min, i
            elif arrays[i][0] < arrays[second_min][0]:
                second_min = i

        if best_max != best_min:
            return arrays[best_max][-1] - arrays[best_min][0]
        else:
            return max(
                arrays[best_max][-1] - arrays[second_min][0],
                arrays[second_max][-1] - arrays[best_min][0],
            )
