# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root
        queue = [root]
        while len(queue) > 0:
            tmp = queue[0]
            if tmp.right is not None:
                queue.append(tmp.right)
            if tmp.left is not None:
                queue.append(tmp.left)
            tmp.left, tmp.right = tmp.right, tmp.left
            queue.pop(0)
        return root