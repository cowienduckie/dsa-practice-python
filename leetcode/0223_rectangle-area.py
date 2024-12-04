class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        # Compute overlapping sides
        left, bot, right, top = (
            max(ax1, bx1),
            max(ay1, by1),
            min(ax2, bx2),
            min(ay2, by2),
        )

        # Compute total area
        return (
            self.compute_rectangle_area(ax1, ay1, ax2, ay2)
            + self.compute_rectangle_area(bx1, by1, bx2, by2)
            - self.compute_rectangle_area(left, bot, right, top)
        )

    def compute_rectangle_area(self, left: int, bot: int, right: int, top: int) -> int:
        if left < right and bot < top:
            return (right - left) * (top - bot)
        else:
            return 0


print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))  # 45
