from heapq import heappop, heappush
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        arrival_ord = sorted(range(n), key=lambda x: times[x][0])
        empty_seats, taken_seats = list(range(n)), []

        for i in arrival_ord:
            arrival, leave = times[i]

            while taken_seats and taken_seats[0][0] <= arrival:
                heappush(empty_seats, heappop(taken_seats)[1])
            seat = heappop(empty_seats)

            if i == targetFriend:
                return seat
            else:
                heappush(taken_seats, (leave, seat))
