class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        while low <= high:
            mid = (high + low) // 2
            prod = mid * mid
            if prod == x:
                return mid
            elif prod < x:
                low = mid + 1
            else:
                high = mid - 1
        return high
