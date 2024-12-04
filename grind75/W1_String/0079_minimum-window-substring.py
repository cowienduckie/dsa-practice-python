class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base cases
        s_len = len(s)
        t_len = len(t)
        if s_len < t_len:
            return ""

        # Use a dictionary to store occurrences of t
        window = {}
        target = {}
        for i in range(t_len):
            window[s[i]] = window.get(s[i], 0) + 1
            target[t[i]] = target.get(t[i], 0) + 1

        # Check if the t first letters in s are already answer
        def is_valid() -> bool:
            for letter, count in target.items():
                if window.get(letter, 0) < count:
                    return False
            return True

        if is_valid():
            return s[0:t_len]

        # Use 2 pointers to slide the windows from left to right
        l = 0
        min_len = float("inf")
        ans = ""
        for r in range(t_len, s_len):
            # Add the new letter in to tracking dictionary
            window[s[r]] = window.get(s[r], 0) + 1

            # Skip if the current window is not valid
            if not is_valid():
                continue

            # Shorten the windows if the left most letter is safe to be removed
            while s[l] not in target or window[s[l]] > target[s[l]]:
                window[s[l]] -= 1
                l += 1

            # Update the answer
            if r - l + 1 < min_len:
                min_len = r - l + 1
                ans = s[l : r + 1]

        return ans
