class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Define the vowels and create a mapping of each vowel to a unique bit
        vowels = "aeiou"
        vowel_to_bit = {v: 1 << i for i, v in enumerate(vowels)}

        # Initialize the bitmask and the maximum length of the substring
        bitmask = 0
        max_length = 0

        # Dictionary to store the first occurrence of each bitmask
        # Initialize with bitmask 0 at index -1 to handle the edge case
        first_occurrence = {0: -1}

        # Iterate through the string
        for i, char in enumerate(s):
            # If the character is a vowel, update the bitmask
            if char in vowel_to_bit:
                bitmask ^= vowel_to_bit[char]

            # If the bitmask has been seen before, calculate the length of the substring
            if bitmask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[bitmask])
            else:
                # If the bitmask hasn't been seen before, store the current index
                first_occurrence[bitmask] = i

        return max_length
