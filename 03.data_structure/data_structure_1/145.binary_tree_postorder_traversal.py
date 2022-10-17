# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go_traversal(self, root, array):
        if root.left is not None:
            array = self.go_traversal(root.left, array)
        if root.right is not None:
            array = self.go_traversal(root.right, array)
        array.append(root.val)
        return array

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        return self.go_traversal(root, [])