# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None: return None
        node = TreeNode(preorder[0])
        idx = inorder.index(node.val)
        if idx > 0:
            node.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        if idx < len(inorder) - 1:
            node.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return node