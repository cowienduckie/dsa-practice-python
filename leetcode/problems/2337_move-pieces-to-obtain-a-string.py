class Solution:
    """
    Solution using two pointers to iterate over both strings.

    A valid answer is possible if the following conditions are met:
        - Both strings have the same amount of L and R characters.
        - The relative order of L and R characters is the same in both strings.
        - For each pair of L-L or R-R characters, the start's one have to be able to move to the position of target's one.
    """

    def canChange(self, start: str, target: str) -> bool:
        n, i, j = len(start), 0, 0

        # Iterate over both strings, i for start and j for target.
        while i < n and j < n:
            # Find the next non-underscore pair.
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1

            if i < n and j < n:
                # Check if the pair is same character
                if start[i] != target[j]:
                    return False
                # If the pair is L-L, check if the i can move left to meet j
                if start[i] == "L" and i < j:
                    return False
                # If the pair is R-R, check if the i can move right to meet j
                if start[i] == "R" and i > j:
                    return False
                # If the pair is valid, move both pointer for next iteration.
                i += 1
                j += 1

        # Try to skip the trailing underscores.
        while i < n and start[i] == "_":
            i += 1
        while j < n and target[j] == "_":
            j += 1

        # If both pointers reach the end of the strings, the answer is valid.
        return i == j == n
