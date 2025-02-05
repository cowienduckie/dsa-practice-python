class Solution:
    """
    Two strings are almost equal in case
        - There is 0 or 2 diff indices
        - If there are 2 diff indices, they must be swappable
    """

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Count diff indices
        diff = []
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff.append((c1, c2))
                if len(diff) > 2:
                    return False
        # Check if diff indices is 0 or 1
        if len(diff) == 0:
            return True
        if len(diff) == 1:
            return False
        # If there are 2 diff indices, check if they are swappable
        return diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]
