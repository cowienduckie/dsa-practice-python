class Solution:
    """
    Solution using prefix sum and traversing from both directions
    """
    def countCollisions(self, directions: str) -> int:
        # Iterate from left to right, consider only collisions including cars going left
        ans, prev = 0, "X"
        for curr in directions:
            # If a collistion occurred, update answer and make current car stay
            if curr == "L" and prev in "SR":
                ans += 1
                prev = "S"
            else:
                prev = curr
        # Iterate from right to left, consider only collisions including cars going to right
        prev = "X"
        for curr in directions[::-1]:
            # If a collistion occurred, update answer and make current car stay
            if curr == "R" and prev in "SL":
                ans += 1
                prev = "S"
            else:
                prev = curr     
        return ans
