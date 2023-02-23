# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        while head is not None:
            answer.append(head.val)
            head = head.next
        answer.sort(reverse = True)
        result = ListNode(-1)
        cursor = result
        while len(answer) > 0:
            cursor.next = ListNode(answer.pop())
            cursor = cursor.next
        return result.next