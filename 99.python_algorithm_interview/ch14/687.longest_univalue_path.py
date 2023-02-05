# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left is not None and node.val != node.left.val: left = -1
            if node.right is not None and node.val != node.right.val: right = -1
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1
        dfs(root)
        return self.longest