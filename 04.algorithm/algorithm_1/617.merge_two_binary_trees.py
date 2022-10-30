# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None: return root2
        stack = [[root1, root2]]
        while len(stack) > 0:
            tmp1, tmp2 = stack[-1]
            stack.pop()
            if tmp1 is None or tmp2 is None: continue
            tmp1.val += tmp2.val
            if tmp1.left is None:
                tmp1.left = tmp2.left
            else:
                stack.append([tmp1.left, tmp2.left])
            if tmp1.right is None:
                tmp1.right = tmp2.right
            else:
                stack.append([tmp1.right, tmp2.right])
        return root1
