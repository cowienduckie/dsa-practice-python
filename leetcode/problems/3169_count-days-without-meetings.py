from typing import List

class Solution:
    """
    Solution using line sweep

    Time complexity: O(N)
    Space complexity: O(N) -> Memory limit exceeded
    """

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Maintain an array of meeting ranges apply from day 1 to day n
        scheduled = [0] * (days + 2)
        for start, end in meetings:
            scheduled[start] += 1
            scheduled[end + 1] -= 1

        # Iterate from day 1 to day n, apply the scheduled ranges
        meeting_count = 0
        free_days = 0
        for day in range(1, days + 1):
            meeting_count += scheduled[day]
            # If today have no meeting, update answer
            if meeting_count == 0:
                free_days += 1

        return free_days

class Solution:
    """
    Solution using topo sort

    Time complexity: O(Nlog(N))
    Space complexity: O(1)
    """
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Sort the array by starting day
        meetings.sort()

        # Iterate through all meetings and try to find some gap between meeetings
        latest_end = 0
        free_days = 0

        for start, end in meetings:
            # Update free days if some gap days found
            gap = start - latest_end - 1
            free_days += gap if gap > 0 else 0

            # Update latest ending day
            latest_end = max(latest_end, end)

        return free_days + (days - latest_end)


print(Solution().countDays(5, [[2,4],[1,3]]))