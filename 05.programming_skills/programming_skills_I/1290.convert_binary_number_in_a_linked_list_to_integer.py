# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head is not None:
            answer = answer * 2 + head.val
            head = head.next
        return answer