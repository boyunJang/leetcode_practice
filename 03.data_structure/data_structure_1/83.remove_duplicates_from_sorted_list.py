# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_dic = {}
        answer = ListNode(-1)
        cursor = answer
        while head is not None:
            if head.val not in val_dic:
                cursor.next = ListNode(head.val)
                cursor = cursor.next
                val_dic[head.val] = 1
            head = head.next
        return answer.next