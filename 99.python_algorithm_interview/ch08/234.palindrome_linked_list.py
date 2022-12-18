# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp_list = []
        while head is not None:
            tmp_list.append(head.val)
            head = head.next
        if tmp_list == tmp_list[::-1]: return True
        return False