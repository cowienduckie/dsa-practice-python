class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        whites = 0

        # Check the first window with k-length
        for i in range(k):
            if blocks[i] == "W":
                whites += 1

        # Slide the window to the end of blocks
        ans = whites
        for i in range(k, n):
            # Decrease if popped block is white
            if blocks[i - k] == "W":
                whites -= 1
            # Increase if most recent block is white
            if blocks[i] == "W":
                whites += 1
            # Update answer
            ans = min(ans, whites)

        return ans
