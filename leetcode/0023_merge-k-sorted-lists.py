from heapq import heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for head in lists:
            while head:
                heappush(min_heap, head.val)
                head = head.next

        new_head = temp_node = ListNode()
        while min_heap:
            temp_node.next = ListNode(heappop(min_heap), None)
            temp_node = temp_node.next

        return new_head.next
