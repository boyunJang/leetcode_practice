# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go_traversal(self, root, array):
        if root is None: return array
        array = self.go_traversal(root.left, array)
        array.append(root.val)
        array = self.go_traversal(root.right, array)
        return array

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = self.go_traversal(root, [])
        return answer