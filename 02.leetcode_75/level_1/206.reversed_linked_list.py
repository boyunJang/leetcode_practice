# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next

        answer = ListNode(-1)
        cursor = answer
        while stack != []:
            cursor.next = ListNode(stack[-1])
            stack.pop(-1)
            cursor = cursor.next

        return answer.next