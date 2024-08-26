"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = []
        if root:
            stack += [root]
        res = []
        while stack:
            node = stack.pop()
            for child in node.children:
                stack += [child]
            res.append(node.val)
        return res[::-1]