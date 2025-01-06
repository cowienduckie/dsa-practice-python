from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        # Use an array to store prefix sum of balls and diff before index i
        prefix = [(0, 0)] * n
        for i in range(1, n):
            balls, diff = prefix[i - 1]
            # Update total balls and total diff
            balls += 1 if boxes[i - 1] == "1" else 0
            diff += balls
            # Update prefix sum
            prefix[i] = (balls, diff)

        # Use an array to store suffix sum of balls and diff before index i
        suffix = [(0, 0)] * n
        for i in range(n - 2, -1, -1):
            balls, diff = suffix[i + 1]
            # Update total balls and total diff
            balls += 1 if boxes[i + 1] == "1" else 0
            diff += balls
            # Update suffix sum
            suffix[i] = (balls, diff)

        # Create answer calc total diff before and after each index i
        return [p[1] + s[1] for p, s in zip(prefix, suffix)]
