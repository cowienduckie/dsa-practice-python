# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        # Count number of nodes in list -> n
        n = self.count_nodes(head)
        ans = []

        # If n <= k -> Return each node as a part, fill leftover with null
        if n <= k:
            while k != 0:
                if head != None:
                    ans.append(head)

                    prev, head, prev.next = head, head.next, None
                else:
                    ans.append(None)
                k -= 1
            return ans

        # Otherwise -> Calculate the size of each part should be
        # Traverse through the list, split it into k parts
        large_group_count = n - (n // k) * k
        node = head

        for i in range(k):
            ans.append(node)
            part_size = n // k + (1 if i < large_group_count else 0)
            node = self.traverse_nodes(node, part_size - 1)
            prev, node, prev.next = node, node.next, None

        return ans

    def count_nodes(self, head: Optional[ListNode]) -> int:
        count = 0
        node = head
        while node is not None:
            node = node.next
            count += 1
        return count

    def traverse_nodes(self, node: Optional[ListNode], step: int) -> Optional[ListNode]:
        while step > 0:
            node = node.next
            if node is None:
                break
            else:
                step -= 1
        return node
