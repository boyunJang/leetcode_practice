# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None: return False
        num_dic = {root.val : 1}
        queue = [root]
        while len(queue) > 0:
            tmp = queue[0]
            if tmp.left is not None:
                if k - tmp.left.val in num_dic: return True
                num_dic[tmp.left.val] = 1
                queue.append(tmp.left)
            if tmp.right is not None:
                if k - tmp.right.val in num_dic: return True
                num_dic[tmp.right.val] = 1
                queue.append(tmp.right)
            queue.pop(0)
        return False