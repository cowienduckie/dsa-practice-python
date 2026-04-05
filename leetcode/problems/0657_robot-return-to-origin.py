from typing import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Count the frequency of each move and check if pairs of moves cancel each other out
        cnt = Counter(moves)
        return cnt["L"] == cnt["R"] and cnt["U"] == cnt["D"]
