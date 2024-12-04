from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Use a dummy node as temporary head
        new_head = ListNode()
        new_tail = new_head

        # Traverse both lists, compare the values, and append the smaller value
        while list1 and list2:
            if list1.val < list2.val:
                new_tail.next = list1
                list1 = list1.next
            else:
                new_tail.next = list2
                list2 = list2.next

            new_tail = new_tail.next

        # Append the remaining nodes in the leftover list
        while list1:
            new_tail.next = list1
            list1 = list1.next
            new_tail = new_tail.next

        while list2:
            new_tail.next = list2
            list2 = list2.next
            new_tail = new_tail.next

        return new_head.next
