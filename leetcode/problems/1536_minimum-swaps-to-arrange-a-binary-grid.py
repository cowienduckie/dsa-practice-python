from typing import List


class Solution:
    """
    Solution using greedy approach
    
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        arr = []
        # Compute the number of trailing zeros for each row
        for r in range(n):
            suffix = 0
            for c in range(n - 1, -1, -1):
                if grid[r][c] != 0:
                    break
                suffix += 1
            arr.append(suffix)

        # Count the number of swaps needed to arrange the rows in the required order
        swap = 0
        for i in range(n - 1):
            # Find the closest row with enough trailing zeros
            j = i
            while j < n and arr[j] < n - i - 1:
                j += 1
            # If no such row is found, it's impossible to arrange the grid
            if j == n:
                return -1
            # Add the number of swaps needed to move the row to the correct position
            swap += j - i
            # Move the row to the correct position by swapping it with the rows above it
            while j > i:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
        return swap

            
