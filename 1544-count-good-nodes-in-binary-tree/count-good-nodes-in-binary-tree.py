# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, curMax):
            nonlocal count
            if not root:
                return
            
            if root.val >= curMax:
                count += 1
            
            dfs(root.left, max(curMax, root.val))
            dfs(root.right, max(curMax, root.val))
        
        dfs(root, root.val)
        return count
