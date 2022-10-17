# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go_preorder(self, root, array):
        if root is None: return array
        array.append(root.val)
        array = self.go_preorder(root.left, array)
        array = self.go_preorder(root.right, array)
        return array

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = self.go_preorder(root, [])
        return answer