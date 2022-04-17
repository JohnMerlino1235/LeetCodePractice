# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head:
            temp_node = head
            head = head.next
            temp_node.next = previous
            previous = temp_node

        return previous
