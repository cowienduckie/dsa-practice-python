from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, ans = len(heights) + 1, 0
        minimum = [heights[0]] * n

        heights.append(float("-inf"))
        ans = float("-inf")

        l = 0
        for r in range(1, n):
            # Update the minimum height of the rectangle at the right end
            minimum[r] = min(minimum[r - 1], heights[r])

            # If the height is decreasing, calculate the area of the rectangles
            if heights[r] < heights[r - 1]:
                while l < r:
                    area = (
                        heights[l] * (r - l)
                        if minimum[l] != heights[l]
                        else minimum[l] * r
                    )
                    ans = max(ans, area)
                    l = l + 1

        return ans
