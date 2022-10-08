# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total_cnt = 1
        mid_cnt = 0
        tmp_node = head
        mid_node = head
        while tmp_node.next is not None:
            total_cnt += 1
            tmp_node = tmp_node.next
            if mid_cnt + 1 == int(total_cnt/2):
                mid_node = mid_node.next
                mid_cnt += 1
        return mid_node