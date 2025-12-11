class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        # The computer 0 complexity must be the strictly smallest, otherwise there is no way all computers could be unlocked
        for c in complexity[1:]:
            if c <= complexity[0]:
                return 0
        # If the complexities is valid, all other computers could be unlocked in any orders
        # So, the number of permutations could be (n - 1)! % MOD
        MOD = 1_000_000_007
        n = len(complexity)
        ans = 1
        for num in range(2, n):
            ans = (ans * num) % MOD
        return ans
