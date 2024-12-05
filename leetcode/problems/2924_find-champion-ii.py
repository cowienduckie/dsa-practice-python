from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Use a set to store all teams that lose to at least 1 other team
        # The only left team is the winner, if no winner or more than 1, return -1
        losers = set([w for _, w in edges])
        if len(losers) != n - 1:
            return -1

        for team in range(n):
            if team not in losers:
                return team
