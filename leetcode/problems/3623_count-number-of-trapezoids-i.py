class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        memo = defaultdict(int)
        for x, y in points:
            memo[y] += 1
        
        ans, prefix, MOD = 0, 0, 1_000_000_007
        for points in memo.values():
            edges = points * (points - 1) // 2
            ans = (ans + edges * prefix) % MOD
            prefix = (prefix + edges) % MOD
        
        return ans
