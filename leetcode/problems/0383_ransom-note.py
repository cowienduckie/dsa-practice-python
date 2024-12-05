class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Base cases
        if len(ransomNote) > len(magazine):
            return False

        # Count occurrences of all letters in magazine
        char_dict = {}
        for char in magazine:
            char_dict[char] = char_dict.get(char, 0) + 1

        # Use all letters in char_dict to construct ransomNote
        for char in ransomNote:
            if char_dict.get(char, 0) == 0:
                return False
            char_dict[char] -= 1

        return True
