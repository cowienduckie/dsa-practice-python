from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        stone, block, empty = "#", "*", "."
        ans = [[block] * rows for _ in range(cols)]

        for row in range(rows):
            # For each row, we have two pointers to scan the stones and fill the rotated stones
            fast = slow = cols - 1
            while fast >= 0 and slow >= 0:
                # Fast pointer move first to scan stones until row-ended or blocked
                stones = 0
                while fast >= 0:
                    if box[row][fast] == stone:
                        stones += 1
                    elif box[row][fast] == block:
                        break
                    fast = fast - 1

                # Slow pointer move second to fill the stones after rotated
                while slow > fast:
                    if stones > 0:
                        ans[slow][rows - row - 1] = stone
                    else:
                        ans[slow][rows - row - 1] = empty
                    stones = stones - 1
                    slow = slow - 1

                # Move both pointers to the next cell
                fast = slow = slow - 1

        return ans
