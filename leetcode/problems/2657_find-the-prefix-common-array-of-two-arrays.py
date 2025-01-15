from typing import List


class Solution:
    def __init__(self):
        self.memo = set()
        self.removed = 0

    def try_add(self, num: int) -> None:
        if num not in self.memo:
            self.memo.add(num)
        else:
            self.memo.remove(num)
            self.removed += 1

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            # Try to add A[i] and B[i] to the memo set, if they are already in the set, remove them
            self.try_add(A[i])
            self.try_add(B[i])

            # If any pair exists, they have been removed from the set
            # Append the removed count into answer array
            ans.append(self.removed)
        return ans
