# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        queue = [[root, -math.inf, math.inf]]
        while len(queue) > 0:
            tmp, min_num, max_num = queue[0]
            if tmp.val <= min_num or tmp.val >= max_num: return False
            if tmp.left is not None:
                queue.append([tmp.left, min_num, min(max_num, tmp.val)])
            if tmp.right is not None:
                queue.append([tmp.right, max(min_num, tmp.val), max_num])
            queue.pop(0)
        return True