"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        queue = [[root, 0]]
        dictionary = { 0 : [root] }
        while len(queue) > 0:
            tmp, h = queue.pop(0)
            if tmp.left is not None:
                queue.append([tmp.left, h + 1])
                if h + 1 not in dictionary:
                    dictionary[h + 1] = []
                else:
                    dictionary[h + 1][-1].next = tmp.left
                dictionary[h + 1].append(tmp.left)
            if tmp.right is not None:
                queue.append([tmp.right, h + 1])
                if h + 1 not in dictionary:
                    dictionary[h + 1] = []
                else:
                    dictionary[h + 1][-1].next = tmp.right
                dictionary[h + 1].append(tmp.right)
        return root