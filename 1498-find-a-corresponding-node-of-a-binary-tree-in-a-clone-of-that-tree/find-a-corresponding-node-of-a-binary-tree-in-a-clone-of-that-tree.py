# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(cloned)]
        while stack:
            temp = stack.pop()
            if temp.val == target.val: return temp
            if temp.left: stack.append(temp.left)
            if temp.right: stack.append(temp.right)