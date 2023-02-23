# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(-1)
        cursor = answer
        while head is not None:
            if head.val > cursor.val:
                cursor.next = ListNode(head.val)
                cursor = cursor.next
            else:
                tmp = answer
                while tmp.next is not None and tmp.next.val < head.val:
                    tmp = tmp.next
                tmp_next = tmp.next
                tmp.next = ListNode(head.val)
                tmp.next.next = tmp_next
                cursor = answer
                while cursor.next is not None:
                    cursor = cursor.next
            head = head.next
        return answer.next