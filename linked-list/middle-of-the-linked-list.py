# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Linked List pointer manipulation with dummy head and traversal pointers.
# Tags: linked-list, optimized

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Linked List pointer manipulation with dummy head and traversal pointers.
# Tags: linked-list, optimized
