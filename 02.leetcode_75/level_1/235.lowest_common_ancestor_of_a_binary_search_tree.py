# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return root
        pointer = root
        while pointer:
            if pointer.val > p.val and pointer.val > q.val:
                pointer = pointer.left
            elif pointer.val < p.val and pointer.val < q.val:
                pointer = pointer.right
            else:
                return pointer