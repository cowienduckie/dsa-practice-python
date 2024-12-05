class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        len1, len2 = len(str1), len(str2)
        if len1 < len2:
            return False

        def increase(char: str) -> str:
            return chr(ord(char) + 1) if char != "z" else "a"

        i1 = i2 = 0
        while 0 <= i1 < len1 and 0 <= i2 < len2 and len1 - i1 >= len2 - i2:
            if str2[i2] == str1[i1] or str2[i2] == increase(str1[i1]):
                i2 = i2 + 1
            i1 = i1 + 1

        return i2 == len(str2)
