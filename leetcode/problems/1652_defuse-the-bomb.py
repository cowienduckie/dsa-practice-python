from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        extended = code + code
        extended = extended if k >= 0 else extended[::-1]

        for i in range(len(code)):
            code[i] = sum(extended[i + 1 : i + abs(k) + 1])

        return code if k >= 0 else code[::-1]
