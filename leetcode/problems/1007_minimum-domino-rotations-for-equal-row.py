from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        # Count the occurrences of each number 1-6 in top and bot halves
        # Also count the occurrences of same number in both halves
        top_cnt = [0] * 7
        bot_cnt = [0] * 7
        same_cnt = [0] * 7
        for i in range(n):
            top_cnt[tops[i]] += 1
            bot_cnt[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                same_cnt[tops[i]] += 1

        ans = -1
        for i in range(1, 7):
            # Check if any number 1-6 can be the same in a row
            if top_cnt[i] + bot_cnt[i] - same_cnt[i] == n:
                # Calculate the minimum rotations needed
                ans = min(top_cnt[i] - same_cnt[i], bot_cnt[i] - same_cnt[i])
                break

        return ans
