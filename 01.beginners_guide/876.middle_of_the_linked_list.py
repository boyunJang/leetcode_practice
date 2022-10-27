# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        mid_node = head
        tmp_node = head

        while tmp_node.next is not None and tmp_node.next.next is not None:
            mid_node = mid_node.next
            tmp_node = tmp_node.next.next

        if tmp_node.next is not None:
            mid_node = mid_node.next

        return mid_node