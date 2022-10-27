# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None: return None
        node_cnt = 0
        node_dic = {}
        while head is not None:
            node_cnt += 1
            node_dic[node_cnt] = head
            head = head.next
        remove_num = node_cnt - n + 1
        print(remove_num)
        result = ListNode(-1)
        cursor = result
        for i in range(1, node_cnt + 1):
            print(i, node_dic[i].val)
            if i != remove_num:
                cursor.next = ListNode(node_dic[i].val)
                cursor = cursor.next
        return result.next