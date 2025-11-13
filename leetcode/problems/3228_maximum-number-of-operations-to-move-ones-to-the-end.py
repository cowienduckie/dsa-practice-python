class Solution:
    """
    Greedy solution

    A valid move is only performed if there is a gap of 0-bits on the right of 1-bit. So, in order to maximize the number of operations, every 1-bit must go through all of gaps on its right. This result could be achieved by always perform the move on leftmost possbile 1-bit.

    Time complexity: O(n)
    Space complexity (extra): O(1)
    """
    def maxOperations(self, s: str) -> int:
        gap = ans = 0
        prev = '1'
        for c in s[::-1]:
            if c == '0' and prev == '1':
                gap += 1
            elif c == '1':
                ans += gap
            prev = c
        return ans