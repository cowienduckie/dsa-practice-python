from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the first and last index each character appears as a range [first, last]
        memo = {}
        for i, c in enumerate(s):
            if c not in memo:
                memo[c] = [i, i]
            else:
                memo[c][1] = i

        # Merge the above ranges to make them not collapsed
        not_collapsed = self._merge_ranges(sorted(memo.values()))

        # Compute the size of each range
        return [x[1] - x[0] + 1 for x in not_collapsed]

    def _merge_ranges(self, ranges: List[List[int]]) -> List[List[int]]:
        # Add a dummy value to end the loop
        ranges.append([float("inf"), float("inf")])

        # Iterate through all ranges and merge the collapsed ones
        ans = []
        merging = ranges[0]

        for i in range(1, len(ranges)):
            # If the current range has start after merging range end, finish the merging step
            if ranges[i][0] > merging[1]:
                ans.append(merging)
                merging = ranges[i]
            # Otherwise, merge current range into merging range
            else:
                merging[1] = max(ranges[i][1], merging[1])

        return ans
