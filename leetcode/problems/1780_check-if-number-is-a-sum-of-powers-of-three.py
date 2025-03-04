class Solution:
    """
    Solution using recursion
    """

    def checkPowersOfThree(self, n: int) -> bool:
        # Use DFS to check every single cases
        def dfs(exponent: int, curr: int) -> bool:
            # If a valid configuration found, return True
            if curr == n:
                return True
            # If the exponent outreach the limit
            if exponent > 14:
                return False
            # Try not to take 3^i
            if dfs(exponent + 1, curr):
                return
            # Try to take 3^i
            return dfs(exponent + 1, curr + 3**exponent)

        # Start from 0 and 3^0
        return dfs(0, 0)


class Solution:
    """
    Solution using math
    """

    def checkPowersOfThree(self, n: int) -> bool:
        # Start from 3^14 because n <= 10^7 and 14 < log3(10^7) < 15
        exponent = 14
        while n and exponent >= 0:
            # If n >= 3^exponent, subtract 3^exponent from n
            if n >= 3**exponent:
                n -= 3**exponent
            # Move to the next exponent
            exponent -= 1
        return n == 0
