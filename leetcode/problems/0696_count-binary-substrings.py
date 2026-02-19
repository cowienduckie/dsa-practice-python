class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr_group = prev_group = ans = 0
        curr_bit = None
        for bit in s:
            # Lengthen current group if current bit is matched
            # Otherwise, start a new group
            if bit == curr_bit:
                curr_group += 1
            else:
                prev_group = curr_group
                curr_group = 1
                curr_bit = bit
            # Increase answer if a valid substring could end at current bit
            if curr_group <= prev_group:
                ans += 1
        return ans
