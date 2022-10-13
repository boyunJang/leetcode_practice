# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = [[root, 1]]
        answer = []
        while len(queue) > 0:
            tmp_node = queue[0][0]
            level = queue[0][1]
            queue.pop(0)
            if len(answer) < level:
                answer.append([])
            answer[level-1].append(tmp_node.val)
            if tmp_node.left is not None:
                queue.append([tmp_node.left, level + 1])
            if tmp_node.right is not None:
                queue.append([tmp_node.right, level + 1])
        return answer