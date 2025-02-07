from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_cnt = defaultdict(int)
        color_map = defaultdict(int)
        ans = []
        for ball, new_color in queries:
            old_color = color_map[ball]
            if old_color != 0:
                # Decrease old color's counter
                color_cnt[old_color] -= 1

                # Delete if no ball with old color
                if color_cnt[old_color] == 0:
                    del color_cnt[old_color]

            # Set ball with new color
            color_map[ball] = new_color

            # Increase new color's counter
            color_cnt[new_color] += 1

            # Update answer
            ans.append(len(color_cnt))
        return ans
