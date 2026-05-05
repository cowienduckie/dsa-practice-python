from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # Find tail node and length of linked list
        tail = head
        n = 1
        while tail.next:
            n += 1
            tail = tail.next

        # Reduce unnecessary loops when k > n
        k %= n
        if not k:
            return head

        # Find the pivot after k rotations (placed between curr and prev pointers)
        prev, curr = head, head.next
        for _ in range(n - k - 1):
            prev = prev.next
            curr = curr.next

        # Update the linked list sequence
        prev.next = None
        tail.next = head

        return curr


print(
    Solution()
    .rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    .val
)
