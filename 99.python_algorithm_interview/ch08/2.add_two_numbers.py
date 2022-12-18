# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(-1)
        cursor = answer
        add_num = 0
        while l1 is not None and l2 is not None:
            cursor.next = ListNode(l1.val + l2.val + add_num)
            if cursor.next.val >= 10:
                cursor.next.val -= 10
                add_num = 1
            else:
                add_num = 0
            cursor = cursor.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            cursor.next = ListNode(l1.val + add_num)
            if cursor.next.val >= 10:
                cursor.next.val -= 10
                add_num = 1
            else:
                add_num = 0
            cursor = cursor.next
            l1 = l1.next
        while l2 is not None:
            cursor.next = ListNode(l2.val + add_num)
            if cursor.next.val >= 10:
                cursor.next.val -= 10
                add_num = 1
            else:
                add_num = 0
            cursor = cursor.next
            l2 = l2.next
        if add_num == 1:
            cursor.next = ListNode(1)
        return answer.next