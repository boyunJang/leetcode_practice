# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode(-1)
        cursor = new_head
        while head is not None:
            if head.val != val:
                cursor.next = ListNode(head.val)
                cursor = cursor.next
            head = head.next
        if cursor.next == val:
            cursor.next = None

        return new_head.next