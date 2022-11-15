# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        answer = 0

        queue = [root]
        while len(queue) > 0:
            tmp = queue.pop(0)
            if tmp.left is not None:
                if tmp.left.left is None and tmp.left.right is None:
                    answer += tmp.left.val
                else:
                    queue.append(tmp.left)
            if tmp.right is not None:
                queue.append(tmp.right)

        return answer