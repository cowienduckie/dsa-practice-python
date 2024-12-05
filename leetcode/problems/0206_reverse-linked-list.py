from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(node: Optional[ListNode], parent: ListNode) -> ListNode:
            if not node:
                return parent

            next_node = node.next
            node.next = parent
            return traverse(next_node, node)

        return traverse(head, None)
