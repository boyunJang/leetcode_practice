# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.answer = 10 ** 5
        def DFS(node):
            min_val, max_val = node.val, node.val
            if node.left is not None:
                min_val, max_left = DFS(node.left)
                self.answer = min(self.answer, node.val - max_left)
            if node.right is not None:
                min_right, max_val = DFS(node.right)
                self.answer = min(self.answer, min_right - node.val)

            return min_val, max_val

        _, _ = DFS(root)

        return self.answer