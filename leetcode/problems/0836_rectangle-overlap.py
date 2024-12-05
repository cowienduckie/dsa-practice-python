from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left, bot, right, top = (
            max(rec1[0], rec2[0]),
            max(rec1[1], rec2[1]),
            min(rec1[2], rec2[2]),
            min(rec1[3], rec2[3]),
        )
        return left < right and bot < top


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # left -> bottom -> right -> top respectively
        return (
            rec1[0] < rec2[2]
            and rec1[1] < rec2[3]
            and rec1[2] > rec2[0]
            and rec1[3] > rec2[1]
        )
