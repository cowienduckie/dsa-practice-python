from typing import List


class Solution:
    """
    Brute-force solution with recursion
    """

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ans = float("inf")

        def dfs(i: int, curr_cost: int, end_date: int) -> None:
            if i == len(days):
                nonlocal ans
                ans = min(ans, curr_cost)
                return

            if days[i] <= end_date:
                dfs(i + 1, curr_cost, end_date)
            else:
                dfs(i + 1, curr_cost + costs[0], days[i])
                dfs(i + 1, curr_cost + costs[1], days[i] + 6)
                dfs(i + 1, curr_cost + costs[2], days[i] + 29)

        dfs(0, 0, -1)
        return ans


class Solution:
    """
    Solution using bottom-up DP to store the optimal cost for each day from day 1 to the last day
    """

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Use DP with 1D array to store the optimal cost for each day
        dp = [0] * (days[-1] + 1)
        i = 0
        for day in range(1, days[-1] + 1):
            # If current day no need to travel, skip buying new ticket
            # Otherwise, try to buy a new ticket for today or in the past
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2],
                )
                i += 1
        return dp[-1]
