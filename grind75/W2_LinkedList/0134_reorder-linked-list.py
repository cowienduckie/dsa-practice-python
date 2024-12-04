from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge the two halves
        left, right = head, prev
        while right.next:
            left_next, right_next = left.next, right.next
            left.next = right
            right.next = left_next
            left, right = left_next, right_next


class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
            slow = fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverse(node: Optional[ListNode], parent: ListNode) -> Optional[ListNode]:
            if not node:
                return parent

            next_node = node.next
            node.next = parent
            return reverse(next_node, node)

        def merge(left: Optional[ListNode], right: Optional[ListNode]) -> None:
            while right:
                left_next = left.next
                right_next = right.next

                left.next = right
                right.next = left_next

                left = left_next
                right = right_next

        if not head:
            return

        mid = find_middle(head)
        rev = reverse(mid, None)
        merge(head, rev)


node_values = [1, 2, 3, 4, 5]
head = None

for val in node_values[::-1]:
    head = ListNode(val, head)

Solution1().reorderList(head)

while head:
    print(head.val)
    head = head.next
