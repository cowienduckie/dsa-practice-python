class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Ascending sort the letters by the number of occurrences
        count = {"a": a, "b": b, "c": c}
        letter = ["a", "b", "c"]
        letter.sort(key=lambda x: count[x])

        # Assume that a > b > c, we can initialize a string like "abcabc...abc|abab...ab" by consuming all "b" an "c"
        # abc -> the number of "abc"
        # ab  -> the number of "ab"
        # leftovers -> the number of "a" left
        abc = count[letter[0]]
        ab = count[letter[1]] - count[letter[0]]
        leftovers = count[letter[2]] - count[letter[1]]
        ans = ""

        while abc > 0:
            curr_str = ""
            # If there are leftovers, change "abc" into "aabc"
            if leftovers:
                curr_str += letter[2] * 2 + letter[1]
                leftovers -= 1
            else:
                curr_str += letter[2] + letter[1]

            # If there are leftovers, change "aabc" into "aabac" or "aabaac"
            if leftovers:
                curr_str += letter[2] * min(2, leftovers) + letter[0]
                leftovers -= min(2, leftovers)
            else:
                curr_str += letter[0]

            ans += curr_str
            abc -= 1

        while ab > 0:
            curr_str = ""
            # If there are leftovers, change "ab" into "aab"
            if leftovers:
                curr_str += letter[2] * 2 + letter[1]
                leftovers -= 1
            else:
                curr_str += letter[2] + letter[1]

            ans += curr_str
            ab -= 1

        # If there are leftovers, add "a" or "aa" to the end
        return ans + letter[2] * min(2, leftovers)
