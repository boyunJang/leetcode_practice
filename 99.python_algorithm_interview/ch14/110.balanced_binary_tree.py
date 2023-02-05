# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer: bool = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def dfs(node):
            if node is None: return 0
            if node.left is None:
                left = 0
            else:
                left = dfs(node.left)
            if node.right is None:
                right = 0
            else:
                right = dfs(node.right)
            if left - right > 1 or right - left > 1:
                print(node.val)
                self.answer = False
            return max(left, right) + 1

        dfs(root)
        return self.answer