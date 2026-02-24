class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        # Base case
        if k >= n:
            return False

        # Prepare first state of k-length substring in s
        curr = 0
        for i in range(0, k):
            if s[i] == "1":
                curr |= 1 << (k - 1 - i)

        # Store all states of k-length substring in s
        seen = set([curr])
        for i in range(k, n):
            # Toggle off bit k-1 in current state
            curr &= ~(1 << (k - 1))
            # Shift all bits to the left
            curr = curr << 1
            # If current bit is 1, set it
            if s[i] == "1":
                curr |= 1
            # Try add current state to hash set
            if curr not in seen:
                seen.add(curr)
        # Compare size of hash set if it can reach 2^k (all possible combination of k-length)
        return len(seen) == 2**k
