# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:

        if not head and not head.next:
            return

        dummy = ListNode(0, head)

        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Linked List pointer manipulation with dummy head and traversal pointers.
# Tags: linked-list, optimized
