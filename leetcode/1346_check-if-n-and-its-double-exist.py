from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        memo = set()
        for num in arr:
            if num * 2 in memo or (num % 2 == 0 and num / 2 in memo):
                return True
            memo.add(num)
        return False
