from typing import Dict


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Transform string S to num_str of numbers
        num_str = ""
        char_dict: Dict[str, int] = {
            chr(i): str(i - ord("a") + 1) for i in range(ord("a"), ord("z") + 1)
        }

        for char in s:
            num_str += char_dict[char]

        # Loop k times to calculate sum of digits
        for _ in range(k):
            num_str = str(sum(int(num) for num in num_str))

        return int(num_str)


Solution().getLucky("iiii", 1)
