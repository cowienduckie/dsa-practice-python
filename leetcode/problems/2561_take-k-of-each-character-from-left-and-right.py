class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)

        # Count the number of each character in the prefix
        count = [0, 0, 0]
        for char in s:
            count[ord(char) - ord("a")] += 1

        if min(count) < k:
            return -1

        # Use sliding window to find answer
        l, ans = 0, float("inf")

        for r in range(n):
            count[ord(s[r]) - ord("a")] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord("a")] += 1
                l += 1
            ans = min(ans, n - (r - l + 1))

        return ans


print(Solution.takeCharacters(Solution, "aabaaaacaabc", 2))  # 8
print(Solution.takeCharacters(Solution, "a", 1))  # -1
print(Solution.takeCharacters(Solution, "aabbccca", 2))  # 6
