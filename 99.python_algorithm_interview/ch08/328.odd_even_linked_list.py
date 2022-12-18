# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(-1)
        even = ListNode(-1)
        odd_c, even_c = odd, even
        iter = 0
        while head is not None:
            iter += 1
            if iter % 2 == 0:
                even_c.next = ListNode(head.val)
                even_c = even_c.next
            else:
                odd_c.next = ListNode(head.val)
                odd_c = odd_c.next
            head = head.next

        odd_c.next = even.next
        return odd.next