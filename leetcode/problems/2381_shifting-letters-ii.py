from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        # Use a difference array to store changes of multiple ranges
        # By updating 2 boundaries but not every inner elements
        diff = [0] * (n + 1)
        for start, end, is_forward in shifts:
            if is_forward:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        # Apply the shifts from left to right
        letters = "abcdefghijklmnopqrstuvwxyz"
        ans = []
        curr_shifts = 0
        for i in range(n):
            curr_shifts = (curr_shifts + diff[i]) % 26
            if curr_shifts < 0:
                curr_shifts += 26
            ans.append(letters[(ord(s[i]) - ord("a") + curr_shifts) % 26])

        return "".join(ans)
