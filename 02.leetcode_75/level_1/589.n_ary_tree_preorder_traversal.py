"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        stack = [root]
        answer = []
        while len(stack) > 0:
            tmp = stack[-1]
            answer.append(tmp.val)
            child = tmp.children
            stack.pop()
            while len(child) > 0:
                stack.append(child[-1])
                child.pop()

        return answer