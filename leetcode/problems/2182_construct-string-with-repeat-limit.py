class Solution:
    def repeatLimitedString(self, s: str, limit: int) -> str:
        # Count all characters in string s
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord("a")] += 1

        # Greedy choose from z to a
        ans = []
        for i in range(25, -1, -1):
            cnt = limit
            while letters[i] and cnt:
                # Add the greatest letter i
                ans.append(chr(ord("a") + i))
                letters[i] -= 1
                cnt -= 1

                # If we can still add more greatest letter i
                # Or there is none left, skip interval
                if cnt or not letters[i]:
                    continue

                # Otherwise, add one of second greatest letter j if possible
                # To reset the consecutive letter i
                for j in range(i - 1, -1, -1):
                    if letters[j]:
                        ans.append(chr(ord("a") + j))
                        letters[j] -= 1
                        cnt = limit
                        break

        # Join the answer characters
        return "".join(ans)
