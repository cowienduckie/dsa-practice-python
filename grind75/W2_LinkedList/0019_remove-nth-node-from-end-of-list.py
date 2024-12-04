from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def traverse(node: Optional[ListNode], prev: Optional[ListNode]) -> int:
            if not node:
                return 0

            pos_from_tail = traverse(node.next, node) + 1
            if pos_from_tail == n and prev:
                prev.next = node.next

            return pos_from_tail

        return head if traverse(head, None) != n else head.next
