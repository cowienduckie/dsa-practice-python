from typing import List


class Solution:
    """
    Solution using mono stack to store the indices of the heights from left to right and right to left
    """

    def trap(self, height: List[int]) -> int:
        n, ans = len(height), 0
        # Compute prefix sum of area ending at each index i
        prefix = [0] * n
        for i in range(n):
            prefix[i] = prefix[i - 1] + height[i]

        # Helper functions to calculate the trapped water area
        def calculate_trapped_water(stack: List[int]) -> int:
            """
            Args:
                stack: List of indices of heights in mono stack (top of stack must be the right-most index)
            """
            trapped, l, r = 0, 0, stack.pop()
            while stack:
                l = stack.pop()
                # Calculate the area between them
                max_water_area = min(height[l], height[r]) * (r - l - 1)
                middle_area = prefix[r] - prefix[l] - height[r]

                # Calculate trapped water area
                water_area = max_water_area - middle_area

                # Update the values
                trapped += water_area if water_area > 0 else 0
                r = l
            return trapped

        # Store the heights in a mono stack from left to right
        stack = []
        for i in range(n):
            if not stack or height[i] >= height[stack[-1]]:
                stack.append(i)
        ans += calculate_trapped_water(stack)

        # Store the heights in a mono stack from right to left
        stack = []
        for i in range(n - 1, -1, -1):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
        ans += calculate_trapped_water(stack[::-1])

        return ans


class Solution:
    """
    Optimized solution using two pointers
    """

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        ans = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                ans += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                ans += max(0, right_max - height[right])

        return ans
