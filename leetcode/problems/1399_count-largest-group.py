from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Count the number of occurrences of each digit sum
        memo = defaultdict(int)
        for num in range(1, n + 1):
            s = sum([int(d) for d in str(num)])
            memo[s] += 1

        # Find the maximum count and count how many groups have that count
        ans = 0
        max_cnt = max(memo.values())
        for v in memo.values():
            if v == max_cnt:
                ans += 1
        return ans
