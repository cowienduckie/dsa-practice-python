from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add a block with negative height to clean up the stack
        heights.append(-1)

        # Use increasing mono stack to maintain the right-most indices of blocks
        ans = 0
        stack = []
        for i in range(len(heights)):
            # Update the mono stack and compute the maximum area using each block as center
            while stack and heights[stack[-1]] >= heights[i]:
                # Take height and width of the area
                h = heights[stack.pop()]
                w = (i - stack[-1] - 1) if stack else i
                # Update final answer
                ans = max(ans, h * w)
            stack.append(i)

        return ans
