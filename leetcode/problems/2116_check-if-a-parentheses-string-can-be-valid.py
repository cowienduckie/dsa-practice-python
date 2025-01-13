class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        # Base cases: Odd length string can't be valid
        if n & 1:
            return False
        # Iterate from left to right, count for open brackets and flexible brackets
        opening = flexible = 0
        for i in range(n):
            # Count for flexible brackets
            if locked[i] == "0":
                flexible += 1
            # Count for open brackets
            elif s[i] == "(":
                opening += 1
            # If we have a closing bracket at index i, check if we can form a valid string from 0 to i
            elif s[i] == ")":
                if opening > 0:
                    opening -= 1
                elif flexible > 0:
                    flexible -= 1
                else:
                    return False

        # Iterate from right to left, for every flexible brackets, we assume them all as closing brackets
        closing = 0
        for i in range(n - 1, -1, -1):
            # Assume all flexible brackets as closing brackets
            if locked[i] == "0":
                closing += 1
                flexible -= 1
            # If we have a opening bracket at index i, check if we can form a valid string from i to n - 1
            elif s[i] == "(":
                if closing > 0:
                    closing -= 1
                    opening -= 1
                else:
                    return False
            # Count for closing brackets
            elif s[i] == ")":
                closing += 1
            # If we complete the fixed brackets early, break the loop
            if flexible == opening == 0:
                return True
        return not opening > 0
