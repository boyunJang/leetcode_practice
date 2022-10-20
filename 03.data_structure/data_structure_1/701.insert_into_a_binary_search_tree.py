# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return TreeNode(val = val)
        cursor = root
        while True:
            if cursor.val > val:
                if cursor.left is not None:
                    cursor = cursor.left
                else:
                    cursor.left = TreeNode(val = val)
                    return root
            elif cursor.val < val:
                if cursor.right is not None:
                    cursor = cursor.right
                else:
                    cursor.right = TreeNode(val = val)
                    return root   