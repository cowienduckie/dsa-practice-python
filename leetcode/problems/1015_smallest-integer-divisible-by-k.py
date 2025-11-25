class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        visited = set()
        remainder, length = 1, 1

        while remainder % k != 0:
            remainder = (remainder * 10 + 1) % k
            if remainder in visited:
                return -1
            visited.add(remainder)
            length += 1

        return length
