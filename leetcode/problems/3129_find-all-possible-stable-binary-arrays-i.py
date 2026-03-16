class Solution:
    MOD = 1_000_000_007

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        max_n = max(zero, one)

        # memo[a][b] = number of ways when current value has `a` remaining
        # and the other value has `b` remaining
        memo = [[None] * (max_n + 1) for _ in range(max_n + 1)]

        def count(curr_remaining: int, other_remaining: int) -> int:
            """
            curr_remaining  = how many of the current digit we still need to place
            other_remaining = how many of the other digit we still need to place
            """
            
            if curr_remaining == 0:
                return 1 if other_remaining == 0 else 0

            if memo[curr_remaining][other_remaining] is not None:
                return memo[curr_remaining][other_remaining]

            # Try placing 1..limit of the current digit
            ways = 0
            for block_size in range(1, min(limit, curr_remaining) + 1):
                ways += count(other_remaining, curr_remaining - block_size)
                ways %= self.MOD

            memo[curr_remaining][other_remaining] = ways
            return ways

        # Start with either 0 or 1
        return (count(zero, one) + count(one, zero)) % self.MOD