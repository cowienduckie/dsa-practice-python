class Solution:
    def maxRunTime(self, n: int, arr: List[int]) -> int:
        m = len(arr)
        arr.sort()
        extra = sum(arr[: m - n])

        for i in range(m - n, m - 1):
            cnt = i - m + n + 1
            gap = (arr[i + 1] - arr[i]) * cnt
            if extra >= gap:
                extra -= gap
            else:
                return arr[i] + extra // cnt
        
        return arr[-1] + extra // n
