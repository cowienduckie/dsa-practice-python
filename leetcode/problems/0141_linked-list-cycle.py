from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        elif head.val == float("inf"):
            return True

        head.val = float("inf")
        return self.hasCycle(head.next)
