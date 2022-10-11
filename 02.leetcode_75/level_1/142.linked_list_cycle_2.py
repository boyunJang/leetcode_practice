# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_dic = {}
        # idx = 0
        while head:
            node_dic[head] = 1
            if head.next in node_dic:
                return head.next
            head = head.next
        return None