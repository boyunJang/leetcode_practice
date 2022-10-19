# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        if root.val == targetSum and root.left is None and root.right is None: return True
        queue = [[root,root.val]]
        while len(queue) > 0:
            tmp = queue[0][0]
            tmp_sum = queue[0][1]
            if tmp.left is not None:
                if tmp_sum + tmp.left.val == targetSum and tmp.left.left is None and tmp.left.right is None: return True
                queue.append([tmp.left, tmp_sum + tmp.left.val])
            if tmp.right is not None:
                if tmp_sum + tmp.right.val == targetSum and tmp.right.left is None and tmp.right.right is None: return True
                queue.append([tmp.right, tmp_sum + tmp.right.val])
            queue.pop(0)

        return False