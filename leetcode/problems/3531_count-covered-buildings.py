class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_min = [float("inf")] * (n + 1)
        row_max = [float("-inf")] * (n + 1)
        col_min = [float("inf")] * (n + 1)
        col_max = [float("-inf")] * (n + 1)

        def is_covered(x: int, y: int) -> bool:
            return row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]

        for x, y in buildings:
            row_min[x] = min(row_min[x], y)
            row_max[x] = max(row_max[x], y)
            col_min[y] = min(col_min[y], x)
            col_max[y] = max(col_max[y], x)
        
        ans = 0
        for x, y in buildings:
            if is_covered(x ,y):
                ans += 1
        return ans
