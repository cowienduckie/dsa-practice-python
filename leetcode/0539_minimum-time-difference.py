from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert the original array into an integer array of total minutes
        # Then, sort the total minutes array
        def toMinutes(timePoint: str) -> int:
            timeParts = timePoint.split(":")
            return int(timeParts[0]) * 60 + int(timeParts[1])

        minutes = [toMinutes(tp) for tp in timePoints]
        minutes.sort()

        # Loop through the array and maintain the minimum diff as answer
        # Initially, the answer is the diff of max time-point and min time-point of the next day
        ans = minutes[0] + 1440 - minutes[-1]  # 1440 = 24 * 60
        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])

        return ans
