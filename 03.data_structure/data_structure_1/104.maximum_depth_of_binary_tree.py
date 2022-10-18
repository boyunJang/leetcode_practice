# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        queue = [[root, 1]]
        max_depth = 1
        while len(queue) > 0:
            tmp_node = queue[0][0]
            tmp_depth = queue[0][1]
            if tmp_depth > max_depth: max_depth = tmp_depth
            if tmp_node.left is not None:
                queue.append([tmp_node.left, tmp_depth + 1])
            if tmp_node.right is not None:
                queue.append([tmp_node.right, tmp_depth + 1])
            queue.pop(0)
        return max_depth