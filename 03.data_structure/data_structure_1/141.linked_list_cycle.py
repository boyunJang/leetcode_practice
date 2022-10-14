# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_dic = {}
        tmp_node = head
        if tmp_node is None: return False
        while True:
            if tmp_node.next is None: return False
            if tmp_node in node_dic : return True
            node_dic[tmp_node] = 1
            tmp_node = tmp_node.next