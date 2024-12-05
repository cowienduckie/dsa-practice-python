from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left_stack = []
        ans = []

        def will_explode(size: int) -> bool:
            while left_stack:
                if size < left_stack[-1]:
                    return True
                else:
                    if size == left_stack.pop():
                        return True
            return False

        for size in asteroids:
            if size > 0:
                left_stack.append(size)
            elif not will_explode(abs(size)):
                ans.append(size)

        return ans + left_stack
