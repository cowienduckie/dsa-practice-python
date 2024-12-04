from typing import List


class Solution:
    """
    Solution using greedy algorithm:
        - Call the ONLY max occurrence task is A with X times, then we can split the array into X - 1 blocks as below:
            A _ _ _ A _ _ _ A _ _ _ A _ _ _ A
        - The minimum length of each block is N to make sure that the rest of tasks can be filled in respectively in descending order

    So, the minimum result could be: X + (X - 1) * N.
    But there are some cases should be considered:
        - If the leftovers are more than block size, just add them normally and we have no need any idle time.
        - If the are multiple tasks have the same X times, just take one of their and put it after the last A
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count occurrences of each possible tasks
        counter = [0] * 26
        for t in tasks:
            counter[ord(t) - ord("A")] += 1

        # Sort the array ascending
        # Then, update answer and array to make sure there is only 1 maximum char
        counter.sort(reverse=True)
        ans = 0
        for i in range(1, 26):
            if counter[i] == counter[0]:
                ans += 1
                counter[i] -= 1

        # Use greedy to fill the rest of array
        return ans + counter[0] + max(n * (counter[0] - 1), sum(counter[1:]))
