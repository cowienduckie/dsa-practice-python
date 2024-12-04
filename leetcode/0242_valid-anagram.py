class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_dict = dict()
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        for char in t:
            if (not char in char_dict) or char_dict[char] == 0:
                return False
            char_dict[char] -= 1
        return True
